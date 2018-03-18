import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot
sys.path.append('../../')
import restore_char_model as rcm


class App(QWidget):

    def make_model_prediction(self):
        shaked_output = rcm.decode_sequence(self.user_input)
        print(shaked_output)

        return shaked_output

    def __init__(self):
        super().__init__()
        self.title = 'Shakey Shakespeare'
        self.left = 180
        self.top = 120
        self.width = 800
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

            # Create widget
        label = QLabel(self)
        pixmap = QPixmap('../shakespeare.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())


            # Create textbox
        textbox = QLineEdit(self)
        textbox.move(20, 20)
        textbox.resize(200, 30)

            # Create button
        shake_button = QPushButton('Shake it!', self)
        shake_button.setToolTip('Lets get shakey')
        shake_button.move(220, 20)
        shake_button.clicked.connect(self.on_shake)

        self.show()

    # Define on-shake action
    @pyqtSlot()
    def on_shake(self):
        self.user_input = self.textbox.text()
        shaked_output = self.make_model_prediction()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
