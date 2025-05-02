import fitz  # PyMuPDF
from pathlib import Path
from pdf2image import convert_from_path

def remove_text_and_convert(pdf_path):
    try:
        # Open PDF with repair mode
        doc = fitz.open(pdf_path, repair=True)
        
        # Create output directories
        output_dir = Path(r'd:\epubpdf')
        images_dir = output_dir / 'images'
        images_dir.mkdir(exist_ok=True)
        
        # Remove text from each page
        for page in doc:
            try:
                # Remove all text
                for item in page.get_text("dict", flags=fitz.TEXT_PRESERVE_IMAGES)["blocks"]:
                    if item["type"] == 0:  # text block
                        rect = fitz.Rect(item["bbox"])
                        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
            except Exception as e:
                print(f"Error processing page {page.number + 1}: {e}")
                continue
        
        # Save text-removed PDF
        cleaned_pdf = output_dir / 'cleaned.pdf'
        doc.save(cleaned_pdf, clean=True)
        doc.close()
        
        # Convert cleaned PDF to images
        images = convert_from_path(cleaned_pdf, dpi=300)
        
        # Save each page
        for i, image in enumerate(images):
            page_num = str(i + 1).zfill(3)
            image_path = images_dir / f'page{page_num}.jpg'
            image.save(image_path, 'JPEG', quality=100)
            print(f"Saved page {page_num}")
            
    except Exception as e:
        print(f"Error processing PDF: {e}")

if __name__ == "__main__":
    pdf_path = r'd:\epubpdf\X05545.pdf'  # Using absolute path
    remove_text_and_convert(pdf_path)