import requests as req
import re
from bs4 import BeautifulSoup as BS

# s = "제 생일은 10월 입니다"
# # pos = s.find("생일은 ")
# # pos += 4

# # print(s[pos])

# # arr = s.split("생일은 ")
# # s = arr[1]

# # print(s.split("월 ")[0])
# bd = s.split("생일은 ")[1].split("월")[0]
# print(bd)

# res = req.get(
#     "https://finance.naver.com/marketindex/")
# html = res.text
# s = html.split('<span class="value">')[1].split('</span>')[0]
# print(s)

# regex 연습
# s = "hi1111"
# print(re.match(r'hi1+', s))

# s = "color"
# print(re.match(r"colou?r", s))

# s = "how are you?"
# print(re.match(r"how are you\?", s))

# s = "이 영화는 A등급 입니다"
# print(s.split("이 영화는 "[1].split("등급")[0]))
# # print(re.match(r"이 영화는 [ABCF]등급 입니다", s))
# print(re.findall(r"이 영화는 ([ABCF])등급 입니다", s))

# querystring 연습
# res = req.get(
#     "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=감자")
# print(res.text)

# beautifulsoup 연습
# url = "https://naver.com"
# res = req.get(url)
# soup = BS(res.text, "html.parser")
# print(soup.title)

# url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED %8F%B0%20%EC%BC%80%EC%9D%B4%EC%8A%A4&cat_id=&frm=NVSHATC"
# res = req.get(url)
# soup = BS(res.text, "html.parser")

# arr = soup.select("ul.list_basis div>a:first-child[title]")
# for a in arr:
#     print(a.get_text(strip=True))

# CSS selector 연습
# url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
# res = req.get(url, headers={
#               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
# soup = BS(res.text, "html.parser")

# for desc in soup.select("div.descriptions-inner"):
#     ads = desc.select("span.ad-badge")
#     if len(ads) == 0:
#         print(desc.select("div.name")[0].get_text(strip=True))
#     else:
#         print("광고")
