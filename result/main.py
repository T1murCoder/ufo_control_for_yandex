import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Управление НЛО')

        self.pixmap = QPixmap('ufo.png')

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.current_position = [0, 0]
        self.label.move(0, 0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.current_position[1] -= 2
        elif event.key() == Qt.Key_Down:
            self.current_position[1] += 2
        elif event.key() == Qt.Key_Right:
            self.current_position[0] += 2
        elif event.key() == Qt.Key_Left:
            self.current_position[0] -= 2
        if self.current_position[0] not in range(0, 451) or self.current_position[1] not in range(0, 451):
            if self.current_position[0] > 450:
                self.current_position[0] = 0
            elif self.current_position[0] < 0:
                self.current_position[0] = 450
            elif self.current_position[1] > 450:
                self.current_position[1] = 0
            elif self.current_position[1] < 0:
                self.current_position[1] = 450
        self.label.move(*self.current_position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())