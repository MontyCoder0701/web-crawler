import requests as req
import re
from bs4 import BeautifulSoup as BS

# 인기 상승 종목 주가
print("-----")
print("인기 상승 종목: 네이버")
print("-----")
print("")

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

# for title in soup.select("a.tltle"):
#     print(title.get_text(strip=True))

for tr in soup.select("table.type_5 tr")[2:]:
    if len(tr.select("a.tltle")) == 0:
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    print(title, price, change)

print("")
print("-----")
print("인기 상승 종목: 구글")
print("-----")
print("")

url = "https://www.google.com/finance/markets/most-active?hl=en"
res = req.get(url)
soup = BS(res.text, "html.parser")

for stat in soup.select("ul.sbnBtf li div.SxcTic"):
    title = stat.select("div.ZvmM7")[0].get_text(strip=True)
    price = stat.select("div.YMlKec")[0].get_text(strip=True)
    change = stat.select("div.JwB6zf")[0].get_text(strip=True)
    print(title, price, change)

# Using regex
url = "https://finance.naver.com/marketindex/"
res = req.get(url)
body = res.text

r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print("-----")
print("환율 계산기")
print("-----")
print("")

for c in captures:
    print(c[0] + ": " + c[1])

print("-----")

usd = float(captures[0][1].replace(",", ""))
won = float(input("달러로 바꾸기 원하는 금액(원)을 입력하세요: "))
dollar = round(float(won/usd), 2)
print(f"현재 {won}원은 {dollar}달러입니다.")

# Using beautifulsoup
# url = "https://finance.naver.com/marketindex/exchangeList.naver"
# res = req.get(url)
# soup = BS(res.text, "html.parser")

# tds = soup.find_all("td")

# names = []
# for td in tds:
#     if len(td.find_all("a")) == 0:
#         continue
#     names.append(td.get_text(strip=True))

# prices = []
# for td in tds:
#     if "class" in td.attrs and "sale" in td.attrs["class"]:
#         prices.append(td.get_text(strip=True))

# Using CSS selector
# names = []
# for td in soup.select("td.tit"):
#     names.append(td.get_text(strip=True))

# prices = []
# for td in soup.select("td.sale"):
#     names.append(td.get_text(strip=True))

# print(names)
# print(prices)
