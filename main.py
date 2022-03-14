import cv2
import math
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys


# Загрузка изображения
def load_image(text):
    image = cv2.imread(f'{text}', cv2.IMREAD_GRAYSCALE)
    return image


# Изменение размеров изображения
def resize_image(image):
    (h, w) = image.shape[:2]
    res_image = cv2.resize(image, (int(w / 1.6), int(h / 1.6)))
    return res_image


# фильтр LoG 3x3
def matrix_3(res_image):

    transform_matrix_3 = ((0, -1, 0), (-1, 4, -1), (0, -1, 0))

    for i in range(1, res_image.shape[0] - 2):
        for j in range(1, res_image.shape[1] - 2):

            g_x = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):

                    g_x += res_image[i + dj][j + di] * transform_matrix_3[1 + di][1 + dj]

            res_image[i][j] = g_x

    cv2.imshow('rom', res_image)
    cv2.waitKey(0)
    # cv2.imwrite('romashka-3x3.jpg', res_image)


# фильтр LoG 7х7
def matrix_7(res_image):

    transform_matrix_7 = ((0, 0, -1, -2, -1, 0, 0),
                         (0, -2, -3, -6, -3, -2, 0),
                         (-1, -3, -8, 0, -8, -3, -1),
                         (-2, -6, 0, 104, 0, -6, -2),
                         (-1, -3, -8, 0, -8, -3, -1),
                         (0, -2, -3, -6, -3, -2, 0),
                         (0, 0, -1, -2, -1, 0, 0))

    for i in range(3, res_image.shape[0] - 4):
        for j in range(3, res_image.shape[1] - 4):

            g_x = 0

            for di in range(-3, 4):
                for dj in range(-3, 4):

                    g_x += res_image[i + di][j + dj] * transform_matrix_7[3 + di][3 + dj]

            res_image[i][j] = g_x / 100

    cv2.imshow('lions1', res_image)
    cv2.waitKey(0)
    # cv2.imwrite('lions-7x7.jpg', res_image)


# фильтр LoG 11x11
def matrix_11(res_image):

    transform_matrix_11 = ((0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0),
                          (0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0),
                          (0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0),
                          (-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1),
                          (-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1),
                          (-2, -9, -23, -1, 103, 180, 103, -1, -23, -9, -2),
                          (-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1),
                          (-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1),
                          (0, -2, -7, -15, -24, -14, -1, -14, -24, -15, -4, -1),
                          (0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0),
                          (0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0))

    for i in range(5, res_image.shape[0] - 6):
        for j in range(5, res_image.shape[1] - 6):

            g_x = 0

            for di in range(-5, 6):
                for dj in range(-5, 6):

                    g_x += res_image[i + di][j + dj] * transform_matrix_11[5 + di][5 + dj]

            res_image[i][j] = g_x / 7000

        cv2.imshow('11x11', res_image)
        cv2.waitKey(0)
        # cv2.imwrite('romashka-11x11.jpg', res_image)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.button_is_checked = True

        self.setWindowTitle("Matrix 3x3 income/result")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.setObjectName("host")
        self.input.setText("host")
        self.input.setMaxLength(10)
        self.input.textEdited.connect(self.label.setText)

        self.button3 = QPushButton("Calculate")
        self.button3.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button3)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window
        self.setCentralWidget(container)

    def set_text(self, text):
        self.label.setText(text)

    def calculate(self):
        text = self.input.text()
        text += '.jpg'
        image = load_image(text)
        res_image = resize_image(image)

        matrix_3(res_image)
        matrix_7(res_image)
        matrix_11(res_image)


if __name__ == '__main__':
    # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения
    app = QApplication(sys.argv)

    # Создаём виджет Qt - окно
    window = MainWindow()
    window.show()

    # Цикл событий
    app.exec()

    # def button_3(self):
    #     text = self.input.text()
    #     text += '.jpg'
    #
    #     self.button3.setText("You already clicked me!")
    #     загрузка изображения
        # image = cv2.imread(f"E:/LabWork1_IMAGES/%s" % (text,), cv2.IMREAD_GRAYSCALE)
        # (h, w) = image.shape[:2]
        # изменение параметров длины и ширины изображения
        # res_image = cv2.resize(image, (int(w / 1.6), int(h / 1.6)))
        # res_image_3 = cv2.resize(image, (int(w / 1.6), int(h / 1.6)))
        #
        # transform_matrix_3 = ((0, -1, 0), (-1, 4, -1), (0, -1, 0))
        #
        # for i in range(1, res_image.shape[0] - 2):
        #     for j in range(1, res_image.shape[1] - 2):
        #         g_x = 0
        #         for di in range(-1, 2):
        #             for dj in range(-1, 2):
        #                 g_x += res_image_3[i + dj][j + di] * transform_matrix_3[1 + di][1 + dj]
        #
        #         res_image[i][j] = math.sqrt(g_x**2 + g_x**2)
        #
        # cv2.imshow('biba', res_image)
        # cv2.waitKey(0)
        #
        # self.button3.setEnabled(False)
        #
        # print(self.button_is_checked)

