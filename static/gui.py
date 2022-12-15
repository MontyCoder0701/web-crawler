import streamlit as st
import streamlit.components.v1 as components
import requests as req
import re
from bs4 import BeautifulSoup as BS
import time

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
    height=150,
)

with st.spinner(text="Live Crawling..."):
    time.sleep(5)
    st.success("Loading complete.")

st.subheader("Most Active Stocks (Live from Naver)")
url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

for tr in soup.select("table.type_5 tr")[2:]:
    if len(tr.select("a.tltle")) == 0:
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    st.write(title, price, change)

st.subheader("Most Active Stocks (Live from Google)")
url = "https://www.google.com/finance/markets/most-active?hl=en"
res = req.get(url)
soup = BS(res.text, "html.parser")

for stat in soup.select("ul.sbnBtf li div.SxcTic"):
    title = stat.select("div.ZvmM7")[0].get_text(strip=True)
    price = stat.select("div.YMlKec")[0].get_text(strip=True)
    change = stat.select("div.JwB6zf")[0].get_text(strip=True)
    st.write(title, price, change)

st.subheader("Exchange Rate (Live from Naver)")
url = "https://finance.naver.com/marketindex/"
res = req.get(url)
body = res.text

r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

for c in captures:
    st.write(c[0] + ": " + c[1])

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
