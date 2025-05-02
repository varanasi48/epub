import cv2
import numpy as np
from pathlib import Path

def detect_text_areas(image_path, output_path):
    # Read image
    img = cv2.imread(str(image_path))
    original = img.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
    
    # Find text regions
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create text coordinates file
    text_coords = []
    
    # Get text coordinates
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        
        # Only process contours that are likely to be text
        if 100 < area < 50000 and w < img.shape[1]//2:
            padding = 5
            x1 = max(0, x-padding)
            y1 = max(0, y-padding)
            x2 = min(img.shape[1], x+w+padding)
            y2 = min(img.shape[0], y+h+padding)
            text_coords.append([x1, y1, x2, y2])
    
    # Save coordinates to a text file
    coords_path = str(output_path).replace('.jpg', '_coords.txt')
    with open(coords_path, 'w') as f:
        for coord in text_coords:
            f.write(f"{coord[0]},{coord[1]},{coord[2]},{coord[3]}\n")
    
    # Save original image
    cv2.imwrite(str(output_path), original)

def process_images():
    input_dir = Path(r'd:\epubpdf\images')
    output_dir = Path(r'd:\epubpdf\images_cleaned')
    output_dir.mkdir(exist_ok=True)
    
    for image_path in input_dir.glob('*.jpg'):
        output_path = output_dir / image_path.name
        print(f"Processing {image_path.name}...")
        detect_text_areas(image_path, output_path)
        print(f"Saved image and coordinates to {output_path}")

if __name__ == "__main__":
    process_images()