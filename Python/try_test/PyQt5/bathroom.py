import sys
from PyQt5.QtWidgets import QDialog, QSystemTrayIcon, QMenu, QAction, QApplication, QLabel, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QColor


def requests_get():
    """Not Empty"""
    url = "https://beta.thejoyrun.com/bathroom/bathrooms?key=0fc37aac2993ed1894b1dfde9ef686b8"

    import requests

    res = requests.get(url, verify=False)

    if res.status_code == 200:
        print(res.text)


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.loadMenu()
        self.initUI()

    def loadMenu(self):
        menuItems = []  # 菜单列表
        menuItems.append({
            "text": "启动",
            "icon": "./icons/set.png",
            "event": self.show,
            "hot": "D"
        })
        menuItems.append({
            "text": "退出",
            "icon": "./icons/close.png",
            "event": self.close,
            "hot": "Q"
        })
        self.trayIconMenu = QMenu(self)  # 创建菜单
        #遍历绑定 显示的文字、图标、热键和点击事件
        #热键可能是无效的 我这里只是为了显示效果而已
        for i in menuItems:
            tmp = QAction(
                QIcon(i["icon"]), i["text"], self, triggered=i["event"])
            tmp.setShortcut(self.tr(i["hot"]))
            self.trayIconMenu.addAction(tmp)

    def initUI(self):
        self.trayIcon = QSystemTrayIcon(self)  # <===创建通知栏托盘图标
        self.trayIcon.setIcon(QIcon("./joyrun/request/pic.ico"))  #<===设置托盘图标

        self.trayIcon.setContextMenu(self.trayIconMenu)  #<===创建右键连接菜单
        self.trayIcon.show()  #<====显示托盘

        self.setWindowIcon(QIcon("./joyrun/request/pic.ico"))  #<===设置窗体图标
        self.setGeometry(300, 300, 180, 300)  # <===设置窗体打开位置与宽高
        self.setWindowTitle('窗体标题')

        self.show()  #<====显示窗体
        # self.hide()#<====隐藏窗体
        # 默认不显示窗体

    # 重写窗体关闭事件,让其点击关闭时隐藏
    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()


class DlgMain(QDialog):
    def addSystemTray(self):
        minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        maximizeAction = QAction(
            "Ma&ximize", self, triggered=self.showMaximized)
        restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        quitAction = QAction("&Quit", self, triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(maximizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("skin/icons/logo.png"))
        self.setWindowIcon(QIcon("skin/icons/logo.png"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
        sys.exit(self.exec_())

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()


from PyQt5.QtGui import QPixmap, QColor


class Tray(QWidget):
    def __init__(self):
        super().__init__()
        # super(self.__class__, self).__init__()

        self.winIconPix = QPixmap(16, 16)
        self.winIconPix.fill(QColor(0, 0, 100))
        self.setWindowIcon(QIcon(self.winIconPix))

        self.tray = QSystemTrayIcon(self)
        self.trayIconPix = QPixmap(16, 16)
        self.trayIconPix.fill(QColor(100, 0, 0))
        self.tray.setIcon(QIcon(self.trayIconPix))
        # self.tray.setIcon(QIcon("C:\\Users\\ShadowMimosa\\Documents\\GitRepository\\Top\\Top\\Joyrun\\request\\icons\\menu2.png"))

        minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        maximizeAction = QAction(
            "Ma&ximize", self, triggered=self.showMaximized)
        restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        quitAction = QAction(
            "&Quit", self, triggered=QApplication.instance().quit)  # 退出APP
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(minimizeAction)
        self.trayMenu.addAction(maximizeAction)
        self.trayMenu.addAction(restoreAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)

        self.tray.show()
        self.show()

    def closeEvent(self, event):
        event.ignore()  # 忽略关闭事件
        self.hide()  # 隐藏窗体


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # ex = Main()
    ex=Tray()

    # sys.exit(app.exec_())
    # import icon
    # tray = QSystemTrayIcon()
    # tray_icon = QIcon(":/img/pic.ico")
    # open('./joyrun/request/pic.ico', 'rb')
    # tray_icon = QIcon("./joyrun/request/pic.ico")
    # icon = QIcon()
    # icon.addPixmap()
    # icon.addPixmap(QPixmap("pic.ico"), QIcon.Normal, QIcon.Off)
    # tray.setIcon(tray_icon)
    # icon_pix = QPixmap(16, 16)
    # icon_pix.fill(QColor(100, 0, 0))
    # tray.setIcon(QIcon(icon_pix))
    # system=QWidget()
    # system.winIconPix=QPixmap(30,10)
    # system.winIconPix.fill(QColor(120,9,22))
    # system.setWindowIcon(QIcon(':/img/pic.ico'))
    # system.show()
    # tray=QSystemTrayIcon(QWidget())
    # tray.show()
    app.exec_()

    # print(a)


# import sys
# from PyQt5.QtWidgets import QWidget, QMenu, QAction, QSystemTrayIcon, QApplication, QVBoxLayout, QListWidget, QListWidgetItem
# from PyQt5.QtGui import QIcon
# from config import menu_items

# class Tray(QWidget):
#     """构建主要窗体"""

#     def __init__(self):
#         """初始化"""
#         super().__init__()

#         self.load_menu()
#         self.init_ui()

#     def load_menu(self):
#         """加载菜单"""

#         menu_items.append({
#             "text": "启动",
#             "icon": "./icons/set.png",
#             "event": self.show,
#             "hot": "D"
#         })
#         menu_items.append({
#             "text": "退出",
#             "icon": "./icons/close.png",
#             "event": self.close,
#             "hot": "Q"
#         })

#         self.tray_menu = QMenu(self)

#         for value in menu_items:
#             tmp = QAction(
#                 QIcon(value["icon"]),
#                 value["text"],
#                 self,
#                 triggered=value["event"])
#             tmp.setShortcut(self.tr(value["hot"]))

#             self.tray_menu.addAction(tmp)

#     def load_list(self):
#         """"""
#         lv = QListWidget()
#         for index in range(len(menu_items)):
#             value = menu_items[index]
#             if not 'icon' in value.keys():
#                 value["icon"] = None
#             if not 'event' in value.keys():
#                 value["event"] = self.show
#             if not 'hot' in value.keys():
#                 value["hot"] = 'None'
#             qlv = QListWidgetItem(
#                 QIcon(value["icon"]),
#                 self.tr(value["text"]) + " (" + value["hot"] + ")")
#             qlv.event = value["event"]
#             lv.insertItem(index + 1, qlv)
#         lv.itemDoubleClicked.connect(self.dbclickItem)
#         self.layout.addWidget(lv)

#     def dbclickItem(self, item):
#         """还不知道是干啥的"""

#         item.event()

#     def init_ui(self):
#         """初始化 UI"""
#         self.tray_icon = QSystemTrayIcon(self)
#         self.tray_icon.setIcon(QIcon("./icons/menu2.png"))

#         self.tray_icon.setContextMenu(self.tray_menu)
#         self.tray_icon.show()

#         self.layout = QVBoxLayout()
#         self.load_list()
#         self.setLayout(self.layout)

#         self.setWindowIcon(QIcon("./icons/menu2.png"))
#         self.setGeometry(300, 300, 220, 300)
#         self.setWindowTitle("joyrun")

#         self.show()
#         import time
#         while True:
#             time.sleep(3)
#             self.load_list()

#     def closeEvent(self, event):
#         if self.tray_icon.isVisible():
#             self.tray_icon.hide()

# if __name__ == "__main__":
    # import os
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))

#     app = QApplication(sys.argv)
#     tray = Tray()

#     app.exec_()