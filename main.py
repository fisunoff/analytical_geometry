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

        self.F = MyFigure(width=5, height=2, dpi=100)
        self.ui.horizontalLayout.addWidget(self.F)

    def solve_metrics(self):
        """В зависимости от ввода находит длину вектора, площадь треугольника или объем пирамиды"""
        A = [self.ui.value_Ax.value(), self.ui.value_Ay.value(), self.ui.value_Az.value()]
        B = [self.ui.value_Bx.value(), self.ui.value_By.value(), self.ui.value_Bz.value()]
        C = [self.ui.value_Cx.value(), self.ui.value_Cy.value(), self.ui.value_Cz.value()]
        D = [self.ui.value_Dx.value(), self.ui.value_Dy.value(), self.ui.value_Dz.value()]
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


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
