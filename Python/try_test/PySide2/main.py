from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = QApplication([])
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
view.ResizeMode(QQuickView.SizeRootObjectToView)
view.show()
app.exec_()

