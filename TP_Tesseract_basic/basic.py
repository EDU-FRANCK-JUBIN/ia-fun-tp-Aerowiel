try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

# print(pytesseract.image_to_string(Image.open('./ressources/image_1.png')))

# print(pytesseract.image_to_data(Image.open('./ressources/image_1.png')))

print(pytesseract.image_to_osd(Image.open('./ressources/image_2.png')))