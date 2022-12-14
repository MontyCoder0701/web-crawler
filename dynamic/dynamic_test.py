from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# Test chromedriver
# browser = webdriver.Chrome("./chromedriver.exe")
# browser.get("https://www.naver.com")
# time.sleep(10)
# browser.close()

# Test Selenium Docker
browser = webdriver.Remote(
    "http://172.17.0.2:4444/wd/hub", DesiredCapabilities.CHROME)
browser.get("https://www.naver.com")
print(browser.title)
browser.close
