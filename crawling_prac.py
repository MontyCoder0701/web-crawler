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

# JSON practice
# data = {
#     "title": "aaa",
#     "author": "joe"
# }

# print(data)
{"data": [{"rank": 1, "rankChange": 0, "symbolCode": "A035720", "code": "KR7035720002", "name": "카카오", "tradePrice": 58100.0, "change": "RISE", "changePrice": 2600.0, "changeRate": 0.0468468468, "chartSlideImage": null, "isNew": false}, {"rank": 2, "rankChange": 0, "symbolCode": "A005930", "code": "KR7005930003", "name": "삼성전자", "tradePrice": 60400.0, "change": "RISE", "changePrice": 1200.0, "changeRate": 0.0202702703, "chartSlideImage": null, "isNew": false}, {"rank": 3, "rankChange": 2, "symbolCode": "A226360", "code": "KR7226360006", "name": "KH 건설", "tradePrice": 598.0, "change": "UPPER_LIMIT", "changePrice": 138.0, "changeRate": 0.3, "chartSlideImage": null, "isNew": false}, {"rank": 4, "rankChange": 2, "symbolCode": "A035420", "code": "KR7035420009", "name": "NAVER", "tradePrice": 195000.0, "change": "RISE", "changePrice": 9500.0, "changeRate": 0.051212938, "chartSlideImage": null, "isNew": false}, {"rank": 5, "rankChange": -1, "symbolCode": "A015760", "code": "KR7015760002", "name": "한국전력", "tradePrice": 21000.0, "change": "RISE", "changePrice": 1650.0, "changeRate": 0.0852713178, "chartSlideImage": null, "isNew": false},
          {"rank": 6, "rankChange": -3, "symbolCode": "A068270", "code": "KR7068270008", "name": "셀트리온", "tradePrice": 180500.0, "change": "RISE", "changePrice": 4000.0, "changeRate": 0.0226628895, "chartSlideImage": null, "isNew": false}, {"rank": 7, "rankChange": 2, "symbolCode": "A112040", "code": "KR7112040001", "name": "위메이드", "tradePrice": 32600.0, "change": "RISE", "changePrice": 2550.0, "changeRate": 0.0848585691, "chartSlideImage": null, "isNew": false}, {"rank": 8, "rankChange": -1, "symbolCode": "A000660", "code": "KR7000660001", "name": "SK하이닉스", "tradePrice": 81500.0, "change": "RISE", "changePrice": 2700.0, "changeRate": 0.0342639594, "chartSlideImage": null, "isNew": false}, {"rank": 9, "rankChange": 1, "symbolCode": "A006400", "code": "KR7006400006", "name": "삼성SDI", "tradePrice": 645000.0, "change": "FALL", "changePrice": 48000.0, "changeRate": 0.0692640693, "chartSlideImage": null, "isNew": false}, {"rank": 10, "rankChange": 0, "symbolCode": "A020120", "code": "KR7020120002", "name": "키다리스튜디오", "tradePrice": 9730.0, "change": "RISE", "changePrice": 1360.0, "changeRate": 0.1624850657, "chartSlideImage": null, "isNew": true}]}
# {data: Array(10)}
# json.data[0].name
