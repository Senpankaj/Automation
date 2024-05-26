import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Read the image
img = cv2.imread('4.png')

# Convert the image from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Use pytesseract to do OCR on the image and save the result to a variable
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)

# Display the image (optional)
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
