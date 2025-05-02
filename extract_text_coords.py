import pdfplumber
import json
from pathlib import Path

def extract_text_coordinates(pdf_path):
    output_dir = Path(r'd:\epubpdf\text_coords')
    output_dir.mkdir(exist_ok=True)
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            words = page.extract_words()
            coords = []
            
            for word in words:
                coords.append({
                    'text': word['text'],
                    'x0': word['x0'],
                    'y0': word['top'],
                    'x1': word['x1'],
                    'y1': word['bottom']
                })
            
            # Save coordinates for each page
            page_coords = output_dir / f'page{str(page_num).zfill(3)}_coords.json'
            with open(page_coords, 'w', encoding='utf-8') as f:
                json.dump(coords, f, indent=2)
            
            print(f"Extracted coordinates for page {page_num}")

if __name__ == "__main__":
    pdf_path = r'X05545.pdf'
    extract_text_coordinates(pdf_path)