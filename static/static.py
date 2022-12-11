import requests as req

# s = "제 생일은 10월 입니다"
# # pos = s.find("생일은 ")
# # pos += 4

# # print(s[pos])

# # arr = s.split("생일은 ")
# # s = arr[1]

# # print(s.split("월 ")[0])
# bd = s.split("생일은 ")[1].split("월")[0]
# print(bd)

res = req.get(
    "https://finance.naver.com/marketindex/")
html = res.text
s = html.split('<span class="value">')[1].split('</span>')[0]
print(s)
