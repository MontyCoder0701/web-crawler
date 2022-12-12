import requests as req
import re
from bs4 import BeautifulSoup as BS

# Using re
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
url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

names = []

for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    names.append(td.get_text(strip=True))

prices = []
for td in tds:
    if "class" in td.attrs and "sale" in td.attrs["class"]:
        prices.append(td.get_text(strip=True))

print(names)
print(prices)
