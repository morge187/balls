import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class Abob(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('balls.ui', self)

        self.btn.clicked.connect(self.draw)

        self.circles = [] # список что бы хранить все шарики

    def create_ball_setting(self):
        # Содзаём все парметры для шарика
        circle_info = {
            'x': random.randint(50, self.width() - 50),
            'y': random.randint(50, self.height() - 50),
            'radius': random.randint(20, 100),
            'color': QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        }
        self.circles.append(circle_info)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for circle_info in self.circles:
            x = circle_info['x']
            y = circle_info['y']
            radius = circle_info['radius']
            color = circle_info['color']

            # Настройка кисти
            painter.setBrush(QBrush(color))
            painter.setPen(Qt.GlobalColor.transparent)

            # Рисуем круг
            painter.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)

        painter.end()

    def draw(self):
        self.create_ball_setting()
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Abob()
    window.show()
    sys.exit(app.exec())
