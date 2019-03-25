import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget, QAction, qApp

# from PyQt5.QtCore import
from PyQt5.QtGui import QIcon


class bathroom_flush(object):
    """处理接口数据"""

    def __init__(
            self,
            url="https://beta.thejoyrun.com/bathroom/bathrooms?key=0fc37aac2993ed1894b1dfde9ef686b8"
    ):
        """初始化类"""
        self.url = url

    def requests_get():
        """Not Empty"""
        import requests

        resp = requests.get(url, verify=False)

        if resp.status_code == 200:
            pass
        else:
            requests_get()

        return resp.text


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.show_menu()
        self.other()

    def show_menu(self):
        """设计托盘的菜单，这里我实现了一个二级菜单"""

        self.menu = QMenu()
        self.menu1 = QMenu()

        self.showAction = QAction("悦跑蹲", self, triggered=self.show_action)
        self.showAction2 = QAction("显示消息2", self, triggered=self.show_action)

        self.quitAction = QAction("退出", self, triggered=self.quit)

        self.menu.addAction(self.showAction)
        self.menu.addAction(self.showAction2)
        #         self.menu1.addAction(self.showAction2)
        self.menu.addMenu(self.menu1)
        self.menu1.setTitle("二级菜单")
        self.menu1.addAction(self.showAction)

        self.menu.addAction(self.showAction)
        #         self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)  # 把鼠标点击图标的信号和槽连接

        self.messageClicked.connect(self.menu_clicked)  # 把鼠标点击弹出消息的信号和槽连接
        # 设置图标
        self.setIcon(QIcon("./icons/menu2.png"))
        self.icon = self.MessageIcon()

    def iconClied(self, reason):
        """鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"""
        if reason in (2, 3):
            power_key = self.parent()

            if power_key.isVisible():
                power_key.hide()
            else:
                power_key.show()

        print(reason)

    def menu_clicked(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def show_action(self):

        self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        """保险起见，为了完整的退出"""

        self.setVisible(False)
        # self.parent().exit()
        qApp.quit()
        # sys.exit()


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        ti = TrayIcon(self)
        # self.hide()
        ti.show()
        self.hide()

    def closeEvent(self, event):
        event.ignore()  # 忽略关闭事件
        self.hide()  # 隐藏窗体


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = window()
    # w.show()
    sys.exit(app.exec_())
