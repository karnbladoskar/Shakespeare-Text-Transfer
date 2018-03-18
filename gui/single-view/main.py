import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'All that glisters is not gold'
        self.left = 180
        self.top = 120
        self.width = 1080
        self.height = 720
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

            # Create widget
        self.label = QLabel(self)
        self.pixmap = QPixmap('../shakespeare.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width, self.height)

            # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(200, 30)

            # Create button
        self.shake_button = QPushButton('Shake it!', self)
        self.shake_button.setToolTip('Lets get shakey')
        self.shake_button.move(220, 20)
        self.shake_button.clicked.connect(self.on_shake)


    # Define on-shake action
    @pyqtSlot()
    def on_shake(self):
        user_input = self.textbox.text()
        print(user_input)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
