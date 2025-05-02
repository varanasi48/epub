import os
import json
import requests

def download_fonts():
    fonts_dir = r'd:\epubpdf\fonts'
    os.makedirs(fonts_dir, exist_ok=True)

    with open(r'd:\epubpdf\fonts.json', 'r', encoding='utf-8') as f:
        fonts_data = json.load(f)

    for font_name in fonts_data:
        # Clean font name (remove subset prefix if exists)
        clean_name = font_name.split('+')[1] if '+' in font_name else font_name
        
        # Create font filenames for different formats
        font_paths = [
            os.path.join(fonts_dir, f"{clean_name}.otf"),
            os.path.join(fonts_dir, f"{clean_name}.ttf")
        ]

        # Skip if font already exists in any format
        if any(os.path.exists(path) for path in font_paths):
            print(f"Font already exists: {clean_name}")
            continue

        # Create empty file to mark font as processed
        with open(font_paths[0], 'wb') as f:
            f.write(b'')
        print(f"Created placeholder for: {clean_name}")

        # Log font info
        font_info = fonts_data[font_name]
        print(f"Font type: {font_info['type']}")
        print(f"Used on pages: {font_info['pages']}")

if __name__ == "__main__":
    download_fonts()
