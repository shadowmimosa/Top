import sys
from PyQt5.QtWidgets import QWidget, QMenu, QAction, QSystemTrayIcon, QApplication, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from config import menu_items


class Tray(QWidget):
    """构建主要窗体"""

    def __init__(self):
        """初始化"""
        super().__init__()

        self.load_menu()
        self.init_ui()

    def load_menu(self):
        """加载菜单"""

        menu_items.append({
            "text": "启动",
            "icon": "./icons/set.png",
            "event": self.show,
            "hot": "D"
        })
        menu_items.append({
            "text": "退出",
            "icon": "./icons/close.png",
            "event": self.close,
            "hot": "Q"
        })

        self.tray_menu = QMenu(self)

        for value in menu_items:
            tmp = QAction(
                QIcon(value["icon"]),
                value["text"],
                self,
                triggered=value["event"])
            tmp.setShortcut(self.tr(value["hot"]))

            self.tray_menu.addAction(tmp)

    def load_list(self):
        """"""
        lv = QListWidget()
        for index in range(len(menu_items)):
            value = menu_items[index]
            if not 'icon' in value.keys():
                value["icon"] = None
            if not 'event' in value.keys():
                value["event"] = self.show
            if not 'hot' in value.keys():
                value["hot"] = 'None'
            qlv = QListWidgetItem(
                QIcon(value["icon"]),
                self.tr(value["text"]) + " (" + value["hot"] + ")")
            qlv.event = value["event"]
            lv.insertItem(index + 1, qlv)
        lv.itemDoubleClicked.connect(self.dbclickItem)
        self.layout.addWidget(lv)

    def dbclickItem(self, item):
        item.event()

    def init_ui(self):
        """初始化 UI"""
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("./icons/menu2.png"))

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

        self.layout = QVBoxLayout()
        self.load_list()
        self.setLayout(self.layout)

        self.setWindowIcon(QIcon("./icons/menu2.png"))
        self.setGeometry(300, 300, 220, 300)
        self.setWindowTitle("joyrun")

        self.show()

    def closeEvent(self, event):
        if self.tray_icon.isVisible():
            self.tray_icon.hide()


if __name__ == "__main__":
    import os
    # os.sys.path
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # a=os.getcwd()
    # sys.path.append(os.path.abspath(__file__))
    # sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # with open("./icons/pic.ico",'w') as fn:
    #     print('true')
    app = QApplication(sys.argv)
    tray = Tray()

    app.exec_()
