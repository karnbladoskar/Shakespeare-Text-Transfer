import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QTabWidget, QVBoxLayout, QTextEdit, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot, Qt
sys.path.append('../../')
import restore_char_model as rcm


class App(QWidget):

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
        self.pixmap = QPixmap('../shakespeare.jpg')
        label.setPixmap(self.pixmap)
        label.resize(self.pixmap.width(), self.pixmap.height())

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(200, 30)

        # Create button
        shake_button = QPushButton('Shake it!', self)
        shake_button.setToolTip('Lets get shakey')
        shake_button.move(220, 20)
        shake_button.clicked.connect(self.on_shake)

        self.returnText = QTextEdit(self)
        self.returnText.setReadOnly(True)
        self.returnText.move(300, 75)
        self.returnText.resize(200, 50)

        self.show()


    # Define on-shake action
    @pyqtSlot()
    def on_shake(self):
        self.user_input = self.textbox.text()
        self.shaked_output = self.make_model_prediction()

        # Clear output
        self.returnText.clear()
        QApplication.processEvents()

        # Append shaked output
        self.returnText.append(self.shaked_output)
        QApplication.processEvents()


    def make_model_prediction(self):
        self.shaked_output = rcm.decode_sequence(self.user_input)
        print(self.user_input)
        print(self.shaked_output)

        return self.shaked_output

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
