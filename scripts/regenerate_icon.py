#!/usr/bin/env python3
"""
Regenerate icon.ico from icon.png in modern ICO format.
This resolves the RC2176 error from old DIB format icons.
"""

from PIL import Image
import os

def regenerate_icon():
    """Convert icon.png to modern ICO format with multiple sizes."""
    icon_png_path = "src-tauri/icons/icon.png"
    icon_ico_path = "src-tauri/icons/icon.ico"
    
    if not os.path.exists(icon_png_path):
        print(f"Error: {icon_png_path} not found")
        return False
    
    try:
        # Open the source image
        img = Image.open(icon_png_path)
        print(f"Loaded source image: {icon_png_path} ({img.size})")
        
        # Create multiple sizes for the ICO file (modern standard sizes)
        # Windows icon format typically includes: 256, 128, 96, 64, 48, 32, 16
        sizes = [
            (256, 256),
            (128, 128),
            (96, 96),
            (64, 64),
            (48, 48),
            (32, 32),
            (16, 16),
        ]
        
        # Resize and create the icon
        icon_images = []
        for size in sizes:
            # Convert to RGBA to ensure compatibility
            rgba_img = img.convert("RGBA") if img.mode != "RGBA" else img
            # Resize with high-quality resampling
            resized = rgba_img.resize(size, Image.Resampling.LANCZOS)
            icon_images.append(resized)
        
        # Save as ICO file with all sizes
        icon_images[0].save(
            icon_ico_path,
            format="ICO",
            sizes=[(img.size, img) for img in icon_images]
        )
        
        print(f"Successfully created modern ICO file: {icon_ico_path}")
        print(f"Icon includes {len(icon_images)} sizes: {sizes}")
        return True
        
    except Exception as e:
        print(f"Error regenerating icon: {e}")
        return False

if __name__ == "__main__":
    import sys
    success = regenerate_icon()
    sys.exit(0 if success else 1)
