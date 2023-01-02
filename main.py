import numpy
from PyQt5 import QtWidgets
import sys
from drawer import MyFigure
from gui import Ui_DockWidget
import re


class MyWindow(QtWidgets.QDockWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.solve_metrics)
        self.ui.pushButton_angle.clicked.connect(self.solve_angles)

        self.F = MyFigure(width=7, height=7, dpi=100)
        self.ui.horizontalLayout.addWidget(self.F)

    def get_data(self) -> tuple[list, list, list, list]:
        """
        Забирает из GUI координаты точек

        :return: Кортеж списков координат точек
        """
        A = [self.ui.value_Ax.value(), self.ui.value_Ay.value(), self.ui.value_Az.value()]
        B = [self.ui.value_Bx.value(), self.ui.value_By.value(), self.ui.value_Bz.value()]
        C = [self.ui.value_Cx.value(), self.ui.value_Cy.value(), self.ui.value_Cz.value()]
        D = [self.ui.value_Dx.value(), self.ui.value_Dy.value(), self.ui.value_Dz.value()]
        return A, B, C, D

    def solve_metrics(self):
        """В зависимости от ввода находит длину вектора, площадь треугольника или объем пирамиды"""
        A, B, C, D = self.get_data()
        coords = {"A": A, "B": B, "C": C, "D": D}
        line = self.ui.metrics_line.text()
        if re.fullmatch(r"[A-D]{2,4}", line):
            match len(line):
                case 2:  # длина вектора
                    p1 = line[0]
                    p2 = line[1]
                    vector_len = ((coords[p1][0] - coords[p2][0]) ** 2 + (coords[p1][1] - coords[p2][1]) ** 2 +
                                  (coords[p1][2] - coords[p2][2]) ** 2) ** 0.5
                    self.ui.result_name.setText("Длина вектора")
                    self.ui.result_line.setText(f"{vector_len:.9f}")
                    self.F.plot(A, B, C, D)
                    self.F.draw_vector(A, B, C, D, p1, p2)
                case 3:  # площадь треугольника
                    p1 = line[0]
                    p2 = line[1]
                    p3 = line[2]
                    vec12 = (coords[p2][0] - coords[p1][0], coords[p2][1] - coords[p1][1],
                             coords[p2][2] - coords[p1][2])  # вектор из 1 точки во 2
                    vec13 = (coords[p3][0] - coords[p1][0], coords[p3][1] - coords[p1][1],
                             coords[p3][2] - coords[p1][2])  # вектор из 1 точки в 3
                    matrix = numpy.array((vec12, vec13))
                    res_matrix = numpy.dot(matrix, matrix.transpose())
                    det = numpy.linalg.det(res_matrix)  # квадрат площади параллелограма, построенного на векторах
                    triangle_square = det ** 0.5 / 2
                    self.ui.result_name.setText("Площадь треугольника")
                    self.ui.result_line.setText(f"{triangle_square:.9f}")
                    self.F.plot(A, B, C, D)
                    self.F.draw_square(A, B, C, D, [p1, p2, p3])
                case 4:  # ориентированный объем пирамиды
                    p1, p2, p3, p4 = line
                    vec12 = (coords[p2][0] - coords[p1][0], coords[p2][1] - coords[p1][1],
                             coords[p2][2] - coords[p1][2])  # вектор из 1 точки во 2
                    vec13 = (coords[p3][0] - coords[p1][0], coords[p3][1] - coords[p1][1],
                             coords[p3][2] - coords[p1][2])  # вектор из 1 точки в 3
                    vec14 = (coords[p4][0] - coords[p1][0], coords[p4][1] - coords[p1][1],
                             coords[p4][2] - coords[p1][2])  # вектор из 1 точки в 4
                    res_matrix = numpy.array((vec12, vec13, vec14))
                    pyramid_volume = numpy.linalg.det(res_matrix) / 6
                    self.ui.result_name.setText("Ориентированный объем\nпирамиды")
                    self.ui.result_line.setText(f"{pyramid_volume:.9f}")
                    self.F.plot(A, B, C, D)
        else:
            self.ui.result_name.setText("Ошибка")
            self.ui.result_line.setText("Ошибка ввода")

    def solve_angles(self):
        """Рассчитывает углы между прямыми и плоскостями"""
        obj1 = self.ui.angle_line_1.text()
        obj2 = self.ui.angle_line_2.text()
        if len(obj2) > len(obj1):
            obj1, obj2 = obj2, obj1  # сначала идет плоскость, потом прямая
        A, B, C, D = self.get_data()
        coords = {"A": A, "B": B, "C": C, "D": D}
        if re.fullmatch(r"[A-D]{2,4}", obj1) and re.fullmatch(r"[A-D]{2,4}", obj2):
            match [len(obj1), len(obj2)]:
                case [2, 2]:  # угол между прямыми
                    vec1 = []
                    vec2 = []
                    for i in range(3):
                        vec1.append(coords[obj1[1]][i] - coords[obj1[0]][i])
                        vec2.append(coords[obj2[1]][i] - coords[obj2[0]][i])
                    len1 = (vec1[0]**2 + vec1[1]**2 + vec1[2]**2)**0.5
                    len2 = (vec2[0]**2 + vec2[1]**2 + vec2[2]**2)**0.5
                    if len1 and len2:
                        angle_cos = (vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]) / (len1 * len2)
                        angle = numpy.arccos(abs(angle_cos))
                        self.ui.result_name_angle.setText("Угол между\nпрямыми")
                        self.ui.result_line_angle_cos.setText(f"acos({angle_cos:.3f})")
                        self.ui.result_line_angle.setText(f"{angle:.3f} рад.")
                        self.F.plot(A, B, C, D)
                        self.F.draw_vector(A, B, C, D, obj1[0], obj1[1])
                        self.F.draw_vector(A, B, C, D, obj2[0], obj2[1])
                    else:
                        self.ui.result_name_angle.setText("Ошибка! Возможно,\nнулевой вектор")
                        self.ui.result_line_angle.setText("Inf")
                        self.F.plot(A, B, C, D)

                case [3, 2]:  # угол между плоскостью и прямой
                    vec11 = []
                    vec12 = []
                    vec2 = []
                    for i in range(3):
                        vec11.append(coords[obj1[1]][i] - coords[obj1[0]][i])  # 1 вектор плоскости
                        vec12.append(coords[obj1[2]][i] - coords[obj1[0]][i])  # 2 вектор плоскости
                        vec2.append(coords[obj2[1]][i] - coords[obj2[0]][i])  # направляющий вектор прямой
                    n1 = [vec11[1] * vec12[2] - vec11[2]*vec12[1],
                          vec11[2] * vec12[0] - vec11[0]*vec12[2],
                          vec11[0] * vec12[1] - vec11[1]*vec12[0]]  # вектор нормали к плоскости
                    len1 = (n1[0]**2 + n1[1]**2 + n1[2]**2)**0.5
                    len2 = (vec2[0]**2 + vec2[1]**2 + vec2[2]**2)**0.5
                    if len1 and len2:
                        angle_sin = (n1[0] * vec2[0] + n1[1] * vec2[1] + n1[2] * vec2[2]) / (len1 * len2)
                        angle = numpy.arcsin(abs(angle_sin))
                        self.ui.result_name_angle.setText("Угол между\nплоскостью\nи прямой")
                        self.ui.result_line_angle_cos.setText(f"asin({angle_sin:.3f})")
                        self.ui.result_line_angle.setText(f"{angle:.3f} рад.")
                        self.F.plot(A, B, C, D)
                        self.F.draw_square(A, B, C, D, list(obj1))
                        self.F.draw_vector(A, B, C, D, obj2[0], obj2[1])

                case [3, 3]:  # угол между плоскостями
                    vec11 = []
                    vec12 = []
                    vec21 = []
                    vec22 = []
                    for i in range(3):
                        vec11.append(coords[obj1[1]][i] - coords[obj1[0]][i])  # 1 вектор 1 плоскости
                        vec12.append(coords[obj1[2]][i] - coords[obj1[0]][i])  # 2 вектор 1 плоскости
                        vec21.append(coords[obj2[1]][i] - coords[obj2[0]][i])  # 1 вектор 2 плоскости
                        vec22.append(coords[obj2[2]][i] - coords[obj2[0]][i])  # 2 вектор 2 плоскости
                    n1 = [vec11[1] * vec12[2] - vec11[2]*vec12[1],
                          vec11[2] * vec12[0] - vec11[0]*vec12[2],
                          vec11[0] * vec12[1] - vec11[1]*vec12[0]]  # вектор нормали к 1 плоскости
                    n2 = [vec21[1] * vec22[2] - vec21[2]*vec22[1],
                          vec21[2] * vec22[0] - vec21[0]*vec22[2],
                          vec21[0] * vec22[1] - vec21[1]*vec22[0]]  # вектор нормали ко 2 плоскости
                    len1 = (n1[0]**2 + n1[1]**2 + n1[2]**2)**0.5
                    len2 = (n2[0]**2 + n2[1]**2 + n2[2]**2)**0.5
                    if len1 and len2:
                        angle_cos = (n1[0] * n2[0] + n1[1] * n2[1] + n1[2] * n2[2]) / (len1 * len2)
                        angle = numpy.arccos(abs(angle_cos))
                        self.ui.result_name_angle.setText("Угол между\nплоскостями")
                        self.ui.result_line_angle_cos.setText(f"acos({angle_cos:.3f})")
                        self.ui.result_line_angle.setText(f"{angle:.3f} рад.")
                        self.F.plot(A, B, C, D)
                        self.F.draw_square(A, B, C, D, list(obj1))
                        self.F.draw_square(A, B, C, D, list(obj2))



app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
