from appium import webdriver
from robot.api.deco import keyword

class MyLibrary:
    def __init__(self):
        self.driver = None

    @keyword("Open Chrome Browser")
    def open_chrome_browser(self):
        """Open Chrome browser on Android device."""
        desired_caps = {
            "platformName": "Android",
            "deviceName": "32007dd24e5e16cf",  # Replace with your device ID
            "browserName": "Chrome",
            "chromedriverExecutableDir": "C:/Users/shant/node_modules/appium-chromedriver/chromedriver/win",  # Path to chromedriver from npm
        }
        self.driver = webdriver.Remote("http://localhost:4723", desired_caps)

    @keyword("Close Chrome Browser")
    def close_chrome_browser(self):
        """Close the Chrome browser."""
        if self.driver:
            self.driver.quit()
