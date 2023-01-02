import numpy
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyFigure(FigureCanvas):
    """Отрисовка пирамиды и дополнительных построений"""

    def __init__(self, width=8, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(projection='3d')
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")
        super(MyFigure, self).__init__(self.fig)  # This sentence is essential, otherwise graphics cannot be displayed

    def plot(self, a: list[float], b: list[float], c: list[float], d: list[float]):
        """
        Рисует пирамиду
        :param a: Координаты точки A
        :param b: Координаты точки B
        :param c: Координаты точки C
        :param d: Координаты точки D

        :return:
        """
        v = numpy.array([a, b, c, d])
        self.ax.clear()
        self.ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        verts = [[v[0], v[1], v[2]], [v[0], v[1], v[3]], [v[0], v[2], v[3]], [v[1], v[2], v[3]]]
        self.ax.text(a[0], a[1], a[2], "a", size=20)
        self.ax.text(b[0], b[1], b[2], "b", size=20)
        self.ax.text(c[0], c[1], c[2], "c", size=20)
        self.ax.text(d[0], d[1], d[2], "d", size=20)

        self.ax.add_collection3d(Poly3DCollection(verts,
                                                  facecolors='cyan', linewidths=1, edgecolors='blue', alpha=.2))
        self.ax.set_aspect('equal')

    def draw_vector(self, a: list[float], b: list[float], c: list[float], d: list[float], start: str, finish: str):
        """
        Рисует вектор на пирамиде
        :param a: Координаты точки A
        :param b: Координаты точки B
        :param c: Координаты точки C
        :param d: Координаты точки D
        :param start: Вершина начала вектора (A, B, C или D)
        :param finish: Вершина конца вектора (A, B, C или D)

        :return:
        """
        dots = {"A": a, "B": b, "C": c, "D": d}
        vector = [dots[finish][0] - dots[start][0], dots[finish][1] - dots[start][1], dots[finish][2] - dots[start][2]]
        self.ax.quiver(dots[start][0], dots[start][1], dots[start][2], vector[0], vector[1], vector[2],
                       color="red", linewidths=3)
        self.ax.set_aspect('equal')

    def draw_square(self, a: list[float], b: list[float], c: list[float], d: list[float], vertexes: list[str]):
        """
        Закрашивает на пирамиде грань
        :param a: Координаты точки A
        :param b: Координаты точки B
        :param c: Координаты точки C
        :param d: Координаты точки D
        :param vertexes: Наименования вершин, на которых построена грань

        :return:
        """
        dots = {"A": a, "B": b, "C": c, "D": d}
        vert = [[dots[vertexes[0]], dots[vertexes[1]], dots[vertexes[2]]], ]
        self.ax.add_collection3d(Poly3DCollection(vert,
                                                  facecolors='red', linewidths=2, edgecolors='red', alpha=.5))
        self.ax.set_aspect('equal')
