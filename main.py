import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor

from design import Ui_MainWindow


class Drawer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Circle drawer")
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.update()

    def paintEvent(self, a0):
        qp = QPainter()
        qp.begin(self)
        self.drawww(qp)
        qp.end()

    def drawww(self, qp):
        qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
        a = randint(50, 150)
        x = randint(0, 50)
        qp.drawEllipse(x, x, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Drawer()
    widget.show()
    app.exec_()
