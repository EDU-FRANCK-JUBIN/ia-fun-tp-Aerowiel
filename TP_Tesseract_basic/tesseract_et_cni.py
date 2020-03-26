try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
import cv2
import numpy as np
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

# grayscale
def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 1)

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

imagePath = './ressources/ci.jpg'
dirCascadeFiles = './opencv/haarcascades_cuda/'
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascadeFile = dirCascadeFiles + 'haarcascade_frontalface_default.xml'
classCascade = cv2.CascadeClassifier(cascadeFile)
faces = classCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)
print("Il y a {0} visage(s)".format(len(faces)))
# Coordonnées des rectangles des visages détectés (x, y, w, h)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# plt.imshow(image)
# plt.show()
# f = faces[0]
# plt.imshow(image[f[1]:f[1]:f[3], f[0]:f[0]+f[2]])

# print(pytesseract.image_to_string(image))

# finalImage = remove_noise(thresholding(grayscale(image)))
# plt.imshow(finalImage)
# plt.show()
# textCI = pytesseract.image_to_string(finalImage)
# print(textCI)

image = cv2.imread(imagePath)
x = 151
y = 49
w = 300
h = 69
plt.imshow(cv2.rectangle(image, (x, y), (w, h), (0,255,0), 2))

region_Nom = image[y:h, x:w]
plt.imshow(region_Nom)
plt.show()

region_Nom = remove_noise(thresholding(grayscale(region_Nom)))
NomCI = pytesseract.image_to_string(region_Nom)
print("Nom = " + NomCI)
