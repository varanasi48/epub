from PIL import Image, ImageOps, ImageFilter
import pytesseract
import cv2
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the path to your image.
image_path = r'hin.jpg'
print(image_path)

# Open the image.
image = Image.open(image_path)

# Convert image to grayscale.
gray_image = ImageOps.grayscale(image)

# Resize the image to enhance details.
scale_factor = 2
resized_image = gray_image.resize(
    (gray_image.width * scale_factor, gray_image.height * scale_factor),
    resample=Image.LANCZOS
)

# Apply adaptive thresholding using the `FIND_EDGES` filter.
thresholded_image = resized_image.filter(ImageFilter.FIND_EDGES)

# Extract text from the preprocessed image.
improved_text = pytesseract.image_to_string(thresholded_image,lang='hin')

# Print the extracted text.
print(improved_text)

output_text_file = "output_text.txt"

with open(output_text_file, "w", encoding="utf-8") as f:
    f.write(improved_text)

print("OCR text saved to:", output_text_file)

# Optional: Save the preprocessed image for review.
thresholded_image.save('preprocessed_image.jpg')