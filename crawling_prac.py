import requests as req

# res = req.get(
#     "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW")
# print(res.text.split("미국 달러 US")[1].split('value="')[1].split('"')[0])

# res = req.get("https://www.naver.com/")
# print(res.text)

# GET / HTTP / 1.1
# Host : www.naver.com

res = req.get("http://api.ipify.org/", headers={"fast": "campus"})
# print(res.status_code)
# print(res.text)
print(res.request.headers)
print(res.elapsed)
# print(res.raw)
