import cv2
import easyocr
import numpy as np
from pathlib import Path

def inpaint_text(image_path, reader):
    img = cv2.imread(str(image_path))
    results = reader.readtext(str(image_path))

    mask = np.zeros(img.shape[:2], dtype="uint8")
    for box in results:
        bbox = box[0]
        x0, y0 = map(int, bbox[0])
        x1, y1 = map(int, bbox[2])
        cv2.rectangle(mask, (x0, y0), (x1, y1), 255, -1)
    
    inpainted_img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    return inpainted_img

def process_images():
    reader = easyocr.Reader(['en'])
    input_dir = Path(r'd:\epubpdf\images')
    output_dir = Path(r'd:\epubpdf\images_cleaned')
    output_dir.mkdir(exist_ok=True)

    for image_path in input_dir.glob('*.jpg'):
        print(f"Processing {image_path.name}...")
        text_removed_image = inpaint_text(image_path, reader)
        output_path = output_dir / image_path.name
        cv2.imwrite(str(output_path), text_removed_image)
        print(f"Saved to {output_path}")

if __name__ == "__main__":
    process_images()