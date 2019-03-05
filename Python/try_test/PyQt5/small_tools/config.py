import os, time


def pr_scrn():  #调用 dll示例
    time.sleep(0.5)
    os.popen('rundll32 .\\script\\截图\\PrScrn.dll PrScrn')


def open_360wifi():  #打开应用程序示例
    os.popen('"C:\\Program Files (x86)\\360\\360AP\\360AP.exe" /menufree')


def open_regedit():  #调用 命令示例
    os.popen('regedit')


def ip_config():
    os.system('''ipconfig & pause''')

def queue_up():
    import bathroom

    


menu_items = [{
    "text": "截图",
    "icon": "./icons/cut.png",
    "event": pr_scrn,
    "hot": "Alt+P"
},
              {
                  "text": "360Wifi",
                  "icon": "./icons/wifi.png",
                  "event": open_360wifi,
                  "hot": "Alt+W"
              },
              {
                  "text": "注册表",
                  "icon": "./icons/regedit.png",
                  "event": open_regedit,
                  "hot": "Alt+R"
              },
              {
                  "text": "ifconfig",
                  "icon": "./icons/ip.png",
                  "event": ip_config,
                  "hot": "Alt+R"
              }]
