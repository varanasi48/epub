import pytesseract
import cv2
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


for i in range(1, 100):
    image_path = f'images/page_{i}.jpg'
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    mask = np.zeros(gray.shape, dtype=np.uint8)
    n_boxes = len(text_data['level'])
    for i in range(n_boxes):
        if text_data['level'][i] == 5: # Level 5 corresponds to word level
            (x, y, w, h) = (text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i])
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
        inpainted_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)        

    cv2.imwrite(f'images/page_{i}.jpg', inpainted_image)