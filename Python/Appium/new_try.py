from appium import webdriver

DESIRED_CAPS = {}
DESIRED_CAPS['platformName'] = 'Android'
DESIRED_CAPS['deviceName'] = '10.99.1.249:6001'
DESIRED_CAPS['platformVersion'] = '9'
# DESIRED_CAPS['deviceName'] = 'd19b1585'
# DESIRED_CAPS['appPackage'] = 'com.taobao.taobao'
# DESIRED_CAPS['appActivity'] = 'com.taobao.tao.welcome.Welcome'

# DRIVER = webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPS)
DESIRED_ = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "platformVersion": "9",
    "noReset": "true",
    "appPackage": "com.google.android.apps.nexuslauncher",
    "appActivity":
    "com.google.android.apps.nexuslauncher.NexusLauncherActivity"
}

# DRIVER.find_element_by_name("1").click()
# DRIVER.find_element_by_name("5").click()
# DRIVER.find_element_by_name("9").click()
# DRIVER.find_element_by_name("delete").click()
# DRIVER.find_element_by_name("9").click()
# DRIVER.find_element_by_name("5").click()
# DRIVER.find_element_by_name("+").click()
# DRIVER.find_element_by_name("6").click()
# DRIVER.find_element_by_name("=").click()

# DRIVER.quit()

# import uiautomator2 as u2

# device = u2.connect('10.99.1.93')
# # device = u2.connect('d19b1585')
# print(device.info)

# device.healthcheck()

# from appium import webdriver
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '9'
# desired_caps['deviceName'] = '10.99.1.93:6002'
# desired_caps['appPackage'] = 'co.runner.app'
# desired_caps['appActivity'] = 'co.runner.app.home_v4.activity.HomeActivityV4'
# desired_caps["noReset"]= "true"
# desired_caps["udid"]='10.99.1.93:6002'

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4'
# desired_caps['deviceName'] = 'FAEUGUBITKMB55EY'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '10.99.1.93:6002'
desired_caps["udid"]='10.99.1.93:6002'
desired_caps['app'] = 'C:/Users/ShadowMimosa/Downloads/joyrun_4.7.0_2019_03_22_14_18_17.apk'
# desired_caps['appPackage'] = 'co.runner.app'
# desired_caps['appActivity'] = 'co.runner.app.home_v4.activity.HomeActivityV4'
desired_caps["noReset"]= "true"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.remove_app('co.runner.app')
driver.install_app(desired_caps['app'])
# driver.install_app(r'D:\PycharmPorjects\appium\psh.apk')
