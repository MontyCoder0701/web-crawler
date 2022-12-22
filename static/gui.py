import streamlit as st
import streamlit.components.v1 as components
import requests as req
import re
from bs4 import BeautifulSoup as BS
import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config(layout="wide")

components.html(
    """
    <div style= "color: #0F52BA; font-weight: bold; text-align: left; font-size: 40px; font-family: Trebuchet MS; box-shadow: 5px 5px 5px #ADD8E6" >
    <img src = "https://img.icons8.com/external-avoca-kerismaker/512/external-Stock-business-avoca-kerismaker.png" style="width: 40px; height: 40px"/>
    Live Stocks 24/7
    <div style= "color: grey; text-align: left; font-size: 10px; font-family: Trebuchet MS;" >
    v.1.0.0      Crawled live from Naver and Google
    <br></br>
    </div>
    </div>
    """,
    height=120,
)

url = "https://www.timeanddate.com/worldclock/south-korea/seoul"
res = req.get(url)
soup = BS(res.text, "html.parser")

for stat in soup.select("div.bk-focus__qlook"):
    now_time = stat.select("span.h1")[0].get_text(strip=True)
    with st.spinner(text="Live Crawling..."):
        time.sleep(5)
        st.success("Crawling complete. Live Crawled Time: " + now_time)

components.html(
    """
    <div style= "color: #000040; font-weight: bold; text-align: left; font-size: 20px; font-family: Trebuchet MS" >
    Current Top Articles
    </div>
    """,
    height=30,
)


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=1000,1000")
options.add_argument("lang=en-GB")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")

driver = get_driver()
driver.get("https://google.com")

wait = WebDriverWait(driver, 5)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


search = find(wait, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
search.send_keys("investment\n")

button = find(
    wait, "#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a > span")
button.click()

headline_1 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#rso > div > div > div:nth-child(1) > div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d")))
st.write(headline_1.text)

headline_2 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#rso > div > div > div:nth-child(2) > div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d")))
st.write(headline_2.text)

headline_3 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#rso > div > div > div:nth-child(3) > div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d")))
st.write(headline_3.text)

components.html(
    """
    <div style= "color: #000040; font-weight: bold; text-align: left; font-size: 20px; font-family: Trebuchet MS" >
    </div>
    """,
    height=10,
)

components.html(
    """
    <div style= "color: #000040; font-weight: bold; text-align: left; font-size: 20px; font-family: Trebuchet MS" >
    Investment Sentiment for 2022
    </div>
    """,
    height=30,
)


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=1000,1000")
options.add_argument("lang=en-GB")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")

driver = get_driver()
driver.get("https://google.com")

wait = WebDriverWait(driver, 10)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


search = find(wait, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
search.send_keys("invest now 2022\n")

positive = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#result-stats")))
st.write("Positive:" + positive.text)

driver.get("https://google.com")
search = find(wait, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
search.send_keys("don't invest now 2022\n")
negative = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#result-stats")))
st.write("Negative:" + negative.text)
driver.close()

# components.html(
#     """
#     <div style= "color: #000040; font-weight: bold; text-align: left; font-size: 20px; font-family: Trebuchet MS" >
#     Historical Interest Rates
#     </div>
#     """,
#     height=30,
# )

# st.sidebar.subheader("Customize Plot Size")
# width = st.sidebar.slider("Plot width", 1, 25, 15)
# height = st.sidebar.slider("Plot height", 1, 25, 2)

# df = pd.read_csv("static/us.csv")
# fig1 = plt.figure(figsize=(width, height))
# ax = sns.kdeplot(data=df, x="INTDSRUSM193N")
# ax.set(xlabel='', ylabel='IR(%)', xticklabels=[],
#        yticklabels=[], title="United States")
# st.pyplot(fig1)

# df = pd.read_csv("static/korea.csv")
# fig2 = plt.figure(figsize=(width, height))
# ax = sns.kdeplot(data=df, x="INTDSRKRM193N")
# ax.set(xlabel='', ylabel='IR(%)', xticklabels=[],
#        yticklabels=[], title="South Korea")
# st.pyplot(fig2)


components.html(
    """
    <div style= "color: #000040; font-weight: bold; text-align: left; font-size: 20px; font-family: Trebuchet MS" >
    </div>
    """,
    height=30,
)

col1, col2, col3 = st.columns([1, 1, 2], gap="large")

with col1:
    st.subheader(":blue[Naver]")
    url = "https://finance.naver.com/sise/lastsearch2.naver"
    res = req.get(url)
    soup = BS(res.text, "html.parser")

    list_one = []

    for tr in soup.select("table.type_5 tr")[2:]:
        if len(tr.select("a.tltle")) == 0:
            continue
        title = tr.select("a.tltle")[0].get_text(strip=True)
        list_one.append(title)
        price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
        change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
        if len(list_one) >= 8:
            break
        st.write(title, price, change)

with col2:
    list_two = []

    st.subheader(":blue[Google]")
    url = "https://www.google.com/finance/markets/most-active?hl=en"
    res = req.get(url)
    soup = BS(res.text, "html.parser")

    for stat in soup.select("ul.sbnBtf li div.SxcTic"):
        title = stat.select("div.ZvmM7")[0].get_text(strip=True)
        list_two.append(title)
        price = stat.select("div.YMlKec")[0].get_text(strip=True)
        change = stat.select("div.JwB6zf")[0].get_text(strip=True)
        if len(list_two) >= 7:
            break
        st.write(title, price, change)

with col3:
    list_three = []
    st.subheader(":blue[Exchange Rate]")
    url = "https://finance.naver.com/marketindex/"
    res = req.get(url)
    body = res.text

    r = re.compile(
        r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
    captures = r.findall(body)

    usd = captures[0][1].replace(",", "")
    won = st.text_input("Convert Won to Dollar: ")

    if len(won) > 0:
        try:
            with st.spinner(text="Converting..."):
                time.sleep(3)
            usd = float(usd)
            won = float(won)
            dollar = round(float(won/usd), 2)
            st.write(f"Currently {won} won is {dollar} dollar(s).")
        except KeyError:
            st.error("Enter a number.")

    for c in captures:
        list_three.append(c)
        if len(list_three) >= 9:
            break
        st.write(c[0] + ": " + c[1])
