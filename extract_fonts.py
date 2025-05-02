import fitz  # PyMuPDF
import json
import os

def extract_fonts_from_pdf(pdf_path):
    fonts_dict = {}
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        fonts = page.get_fonts()
        
        for font in fonts:
            # Clean up font name by removing the subset prefix
            font_name = font[3] if len(font) > 3 else "Unknown"
            if '+' in font_name:
                font_name = font_name.split('+')[1]  # Remove the subset prefix
            
            font_type = font[2] if len(font) > 2 else "Unknown"
            font_encoding = font[1] if len(font) > 1 else "Unknown"
            
            if font_name not in fonts_dict:
                fonts_dict[font_name] = {
                    "type": font_type,
                    "encoding": font_encoding,
                    "pages": [],
                    "embedded": font[6] if len(font) > 6 else False
                }
            
            if page_num + 1 not in fonts_dict[font_name]["pages"]:
                fonts_dict[font_name]["pages"].append(page_num + 1)
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(pdf_path)
    output_file = os.path.join(output_dir, 'fonts.json')
    
    # Save to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(fonts_dict, f, indent=4)
    
    doc.close()
    return fonts_dict

def main():
    pdf_path = r'X05545.pdf'
    fonts = extract_fonts_from_pdf(pdf_path)
    print(f"Found {len(fonts)} unique fonts in the PDF")
    print("Fonts information has been saved to fonts.json")

if __name__ == "__main__":
    main()