import requests as req
import re

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
