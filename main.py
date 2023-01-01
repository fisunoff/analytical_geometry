import numpy
from PyQt5 import QtWidgets
import sys
from gui import Ui_DockWidget
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# Create a matplotlib graphics drawing class
class MyFigure(FigureCanvas):
    def __init__(self, width=8, height=4, dpi=100):
        # Step 1: Create a Create Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # Step 2: Activate the Figure window in the parent class
        super(MyFigure, self).__init__(self.fig)  # This sentence is essential, otherwise graphics cannot be displayed
        # Step 3: Create a subplot for drawing graphics, 111 indicates the subplot number, such as matplot(1,1,1)
        #self.axes = self.fig.add_subplot(111)

    # The fourth step is to draw pictures, [you can draw in this class, you can also draw in other classes]
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = numpy.arange(0.0, 3.0, 0.01)
        s = numpy.sin(2 * numpy.pi * t)
        self.axes0.plot(t, s)

    def plotcos(self):
        t = numpy.arange(0.0, 3.0, 0.01)
        s = numpy.sin(2 * numpy.pi * t)
        self.axes.plot(t, s)


class MyWindow(QtWidgets.QDockWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.solve_metrics)

        self.F = MyFigure(width=5, height=2, dpi=100)
        self.F.plotsin()
        self.ui.horizontalLayout.addWidget(self.F)

    def plotcos(self):
        t = numpy.arange(0.0, 5.0, 0.01)
        s = numpy.cos(2 * numpy.pi * t)
        self.F.axes.plot(t, s)
        self.F.fig.suptitle("cos")

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
                    vector_len = ((coords[p1][0] - coords[p2][0])**2 + (coords[p1][1] - coords[p2][1])**2 +
                                 (coords[p1][2] - coords[p2][2])**2)**0.5
                    self.ui.result_name.setText("Длина вектора")
                    self.ui.result_line.setText(f"{vector_len:.9f}")
                case 3:  # площадь треугольника
                    p1 = line[0]
                    p2 = line[1]
                    p3 = line[2]
                    vec12 = (coords[p2][0] - coords[p1][0], coords[p2][1] - coords[p1][1], coords[p2][2] - coords[p1][2])  # вектор из 1 точки во 2
                    vec13 = (coords[p3][0] - coords[p1][0], coords[p3][1] - coords[p1][1], coords[p3][2] - coords[p1][2])  # вектор из 1 точки в 3
                    matrix = numpy.array((vec12, vec13))
                    res_matrix = numpy.dot(matrix, matrix.transpose())
                    det = numpy.linalg.det(res_matrix)  # квадрат площади параллелограма, построенного на векторах
                    triangle_square = det**0.5 / 2
                    self.ui.result_name.setText("Площадь треугольника")
                    self.ui.result_line.setText(f"{triangle_square:.9f}")
                case 4:
                    p1, p2, p3, p4 = line
                    vec12 = (coords[p2][0] - coords[p1][0], coords[p2][1] - coords[p1][1], coords[p2][2] - coords[p1][2])  # вектор из 1 точки во 2
                    vec13 = (coords[p3][0] - coords[p1][0], coords[p3][1] - coords[p1][1], coords[p3][2] - coords[p1][2])  # вектор из 1 точки в 3
                    vec14 = (coords[p4][0] - coords[p1][0], coords[p4][1] - coords[p1][1], coords[p4][2] - coords[p1][2])  # вектор из 1 точки в 4
                    res_matrix = numpy.array((vec12, vec13, vec14))
                    pyramid_volume = numpy.linalg.det(res_matrix) / 6
                    self.ui.result_name.setText("Ориентированный объем\nпирамиды")
                    self.ui.result_line.setText(f"{pyramid_volume:.9f}")
        else:
            self.ui.result_name.setText("Ошибка")
            self.ui.result_line.setText("Ошибка ввода")


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
