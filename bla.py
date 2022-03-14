import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread('romashka.jpg', cv2.IMREAD_GRAYSCALE)
image_1 = cv2.resize(image, (int(image.shape[1] / 1.6), int(image.shape[0] / 1.6)))
image_3 = cv2.imread('romashka-3x3.jpg', cv2.IMREAD_GRAYSCALE)
image_7 = cv2.imread('romashka-7x7.jpg', cv2.IMREAD_GRAYSCALE)
image_11 = cv2.imread('romashka-11x11.jpg', cv2.IMREAD_GRAYSCALE)

image_weight = int(image_1.shape[0] / 2)
resized_image_weight = int(image_3.shape[0] / 2)


hist_image = []
hist_image_3 = []
hist_image_7 = []
hist_image_11 = []


for i in range(0, image_1.shape[1]):
    hist_image.append(image_1[image_weight][i])

for i in range(0, image_3.shape[1]):
    hist_image_3.append(image_3[resized_image_weight][i])
    hist_image_7.append(image_7[resized_image_weight][i])
    hist_image_11.append(image_11[resized_image_weight][i])


plt.subplot(221)
x = np.arange(0, image_1.shape[1], 1)
plt.plot(x, hist_image)

plt.subplot(222)
x = np.arange(0, image_3.shape[1], 1)
plt.plot(x, hist_image_3)

plt.subplot(223)
x = np.arange(0, image_7.shape[1], 1)
plt.plot(x, hist_image_7)

plt.subplot(224)
x = np.arange(0, image_11.shape[1], 1)
plt.plot(x, hist_image_11)

plt.show()
