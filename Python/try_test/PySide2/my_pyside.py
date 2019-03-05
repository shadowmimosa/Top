import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))


def test1():
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(180, 280)
    widget.show()

    sys.exit(app.exec_())


def test2():

    import sys
    from PySide2.QtWidgets import QApplication, QLabel

    app = QApplication(sys.argv)
    label = QLabel("Hello World!")
    label = QLabel("<font color=red size=40>Hello World!!!!!!</font>")
    label.show()
    app.exec_()


if __name__ == "__main__":
    test2()