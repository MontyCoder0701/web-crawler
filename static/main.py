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
