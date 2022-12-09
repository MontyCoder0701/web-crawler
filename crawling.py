# 환율 크롤링
import requests as req

res = req.get(
    "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW")
print(res.text.split("미국 달러 US")[1].split('value="')[1].split('"')[0])
