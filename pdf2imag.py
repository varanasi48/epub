from pdf2image import convert_from_path
import cv2
import numpy as np
import os

def split_and_save_pages(image, index, output_dir):
    # Convert PIL image to numpy array
    img_np = np.array(image)
    
    # Get dimensions
    height, width = img_np.shape[:2]
    mid_point = width // 2
    
    # Split into left and right pages
    left_page = img_np[:, :mid_point]
    right_page = img_np[:, mid_point:]
    
    # Save left page
    left_num = (index * 2) + 1
    cv2.imwrite(os.path.join(output_dir, f'page{str(left_num).zfill(3)}.jpg'), 
                cv2.cvtColor(left_page, cv2.COLOR_RGB2BGR))
    print(f"Saved left page {left_num}")
    
    # Save right page
    right_num = (index * 2) + 2
    cv2.imwrite(os.path.join(output_dir, f'page{str(right_num).zfill(3)}.jpg'), 
                cv2.cvtColor(right_page, cv2.COLOR_RGB2BGR))
    print(f"Saved right page {right_num}")

def pdf_to_images(pdf_path):
    output_dir = os.path.join(os.path.dirname(pdf_path), "images")
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=300)
    
    # Process each spread
    for i, image in enumerate(images):
        split_and_save_pages(image, i, output_dir)

# Usage
pdf_path = r"d:\epubpdf\X05545.pdf"
pdf_to_images(pdf_path)