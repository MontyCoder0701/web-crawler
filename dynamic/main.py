from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")

chrome = webdriver.Chrome("./chromedriver.exe", options=options)
chrome.get("https://shopping.naver.com")
WebDriverWait(chrome, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[name=query]")))
chrome.close()
