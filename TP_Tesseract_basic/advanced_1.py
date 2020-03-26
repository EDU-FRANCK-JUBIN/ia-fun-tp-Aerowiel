try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
from pytesseract import Output
import cv2

from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

sImage = "./ressources/image_2.png"
img = cv2.imread(sImage)
d = pytesseract.image_to_data(img, output_type=Output.DICT)

NbBoites = len(d['level'])
print("Nombre de boites: " + str(NbBoites))
for i in range(NbBoites):
    # Get coordinates of each box
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    # Show rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img)
# plt.show()

