# from appium import webdriver

# DESIRED_CAPS = {}
# DESIRED_CAPS['platformName'] = 'Android'
# DESIRED_CAPS['deviceName'] = 'emulator-5554'
# DESIRED_CAPS['platformVersion'] = '9'
# # DESIRED_CAPS['deviceName'] = 'd19b1585'
# # DESIRED_CAPS['appPackage'] = 'com.taobao.taobao'
# # DESIRED_CAPS['appActivity'] = 'com.taobao.tao.welcome.Welcome'

# DRIVER = webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPS)

# # DRIVER.find_element_by_name("1").click()
# # DRIVER.find_element_by_name("5").click()
# # DRIVER.find_element_by_name("9").click()
# # DRIVER.find_element_by_name("delete").click()
# # DRIVER.find_element_by_name("9").click()
# # DRIVER.find_element_by_name("5").click()
# # DRIVER.find_element_by_name("+").click()
# # DRIVER.find_element_by_name("6").click()
# # DRIVER.find_element_by_name("=").click()

# DRIVER.quit()

import uiautomator2 as u2

device = u2.connect('10.99.1.93')
# device = u2.connect('d19b1585')
print(device.info)

device.healthcheck()
