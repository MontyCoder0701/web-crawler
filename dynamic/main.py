from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("window-size=1000,1000")
# options.add_argument("no-sandbox")

# chrome = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)
# chrome.get("https://shopping.naver.com")

# wait = WebDriverWait(chrome, 10)


# def find(wait, css_selector):
#     return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


# search = find(wait, "#__next > div > div.header_header__24NVj > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > fieldset > div._gnbSearch_inner_2Zksb > div > input")
# search.send_keys("아이폰 케이스\n")

# # button = find(wait, "#__next > div > div.header_header__24NVj > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > fieldset > div._gnbSearch_inner_2Zksb > div > button._searchInput_button_search_1n1aw > svg > path")
# # button.click()

# time.sleep(3)

# chrome.close()

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")
login_button = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#gnb_login_button > span.gnb_txt")))
print(login_button.text)
login_button.click()

input_id = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#id")))
input_pw = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#pw")))

pyperclip.copy("enter_id")
input_id.send_keys(Keys.CONTROL, "v")
pyperclip.copy("enter_pw")
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")

wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#gnb_logout_button > span.gnb_txt")))

chrome.close()
