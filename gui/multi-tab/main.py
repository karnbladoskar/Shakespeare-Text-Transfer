import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'All that glisters is not gold'
        self.left = 180
        self.top = 120
        self.width = 1080
        self.height = 720
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = Shakespeare(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class Shakespeare(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)

        # Add tabs
        self.tabs.addTab(self.tab1,"Shakespeare")
        self.tabs.addTab(self.tab2,"Yoda")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

            # Create widget
        self.label = QLabel(self)
        self.pixmap = QPixmap('shakespeare.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(2880, 1800)

            # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(200, 30)

            # Create button
        self.shake_button = QPushButton('Shake it!', self)
        self.shake_button.setToolTip('Lets get shakey')
        self.shake_button.move(220, 20)
        self.shake_button.clicked.connect(self.on_shake)

            # Add graphics to layout
        self.tab1.layout.addWidget(self.label)
        self.tab1.layout.addWidget(self.textbox)
        self.tab1.layout.addWidget(self.shake_button)

        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    # Define on-tab
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    # Define on-shake action
    @pyqtSlot()
    def on_shake(self):
        user_input = self.textbox.text()
        print(user_input)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
