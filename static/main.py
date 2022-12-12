import requests as req
import re

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
