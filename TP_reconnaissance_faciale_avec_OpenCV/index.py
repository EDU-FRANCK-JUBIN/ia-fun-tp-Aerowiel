import cv2
import sys
from matplotlib import pyplot as plt


imagePath= "./OpenCv/image2.jpg"
dirCascadeFiles = "./OpenCv/opencv/haarcascades_cuda/"

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cascadeFile = dirCascadeFiles + "haarcascade_frontalface_alt.xml"
cascadeFile = dirCascadeFiles + "haarcascade_frontalface_default.xml"
classCascade = cv2.CascadeClassifier(cascadeFile)

faces = classCascade.detectMultiScale(
    gray,
    scaleFactor=1.5,  # scale factor should be 1.5 instead of 1.1
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)
print("Il y a {0} visage(s)".format(len(faces)))

i = 0
# for(x, y, w, h) in faces:
#     # TEST 1
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     plt.imshow(image)
#     # TEST 2
#     crop_img = image[y:y+h, x:x+w]
#     plt.imshow(crop_img)
#     cv2.imwrite("fichier_resultat_" + str(i) + ".jpg", crop_img)
#
#     i += 1
#
# plt.show()

for i in range(len(faces)):

    print("cadre du visage N°{0} --> {1}".format(i, faces[i]))
    plt.subplot(1, len(faces), i + 1)
    plt.imshow(image[faces[i][1]:faces[i][1]+faces[i][3], faces[i][0]:faces[i][0]+faces[i][2]])

    i += 1

plt.show()


