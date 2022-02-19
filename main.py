import cv2
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


# загрузка изображения
image = cv2.imread('romashka.jpg', cv2.IMREAD_GRAYSCALE)
(h, w) = image.shape[:2]
#
# # изменение параметров длины и ширины изображения
res_image = cv2.resize(image, (int(w/1.6), int(h/1.6)))
res_image_1 = cv2.resize(image, (int(w/1.6), int(h/1.6)))
# res_image_7 = cv2.resize(image, (int(w/1.6), int(h/1.6)))
#
#
# # фильтр LoG 3x3
#
transform_matrix_3 = ((0, -1, 0), (-1, 4, -1), (0, -1, 0))
#
for i in range(1, res_image.shape[0] - 2):
    for j in range(1, res_image.shape[1] - 2):
        g_x = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):

                g_x += res_image_1[i + dj][j + di] * transform_matrix_3[1 + di][1 + dj]

        res_image[i][j] = math.sqrt(g_x**2 + g_x**2)


cv2.imshow('rom', res_image)
cv2.waitKey(0)
cv2.imwrite('romashka-3x3.jpg', res_image)
#
#
# # матрица 7х7
#
# # for i in range(3, res_image_7.shape[0] - 3):
# #     for j in range(3, res_image_7.shape[1] - 3):
# #         g_x = 0
# #         for di in range(-3, 4):
# #             for dj in range(-3, 4):
# #
# #                 g_x += res_image_1[i + di][j + dj] * transform_matrix_7[3 + di][3 + dj]
# #
# #         res_image_7[i][j] = math.sqrt(g_x**2 + g_x**2)
# #
# # cv2.imshow('lions1', res_image_7)
# # cv2.waitKey(0)
#
# #
# # transform_matrix_7 = ((0, 0, -1, -2, -1, 0, 0),
# #                       (0, -2, -3, -6, -3, -2, 0),
# #                       (-1, -3, -8, 0, -8, -3, -1),
# #                       (-2, -6, 0, 104, 0, -6, -2),
# #                       (-1, -3, -8, 0, -8, -3, -1),
# #                       (0, -2, -3, -6, -3, -2, 0),
# #                       (0, 0, -1, -2, -1, 0, 0))
#
# # transform_matrix_11 = ((0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0), (0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0),
# #                        (0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0), (-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1),
# #                        (-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1), (-2, -9, -23, -1, 103, 180, 103, -1, -23, -9, -2))

# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi()
#
#     def setupUi(self):
#         self.setWindowTitle("zxc-pudge")  # заголовок
#         self.move(300, 300)  # положение окна
#         self.resize(200, 200)  # размер окна
#         self.lbl = QLabel('zxc-pudge', self)
#         self.lbl.move(70, 70)
#         self.font = QFont()  # создаём объект шрифта
#         self.font.set_F
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec_())
