# Web-crawler

Web crawler made with Python.  
For both static and dynamic crawling.  

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Virtual environment setup

Install venv

```sh
python3 -m pip install --user virtualenv
```

Create venv

```sh
python3 -m venv env
```

Run venv

```sh
.\env\Scripts\activate
```

## Used libraries

- requests
- beautifulsoup4
- selenium

## Included files

- Static  
Includes code that statically crawls stock name, prices and change from Naver and Google.  
Includes code that statically crawls current exchange rate from Naver.

- Dynamic  
Uses Selenium for to dynamically crawl Chrome.  
If necessary, download Chromedriver that supports your Chrome version. <https://chromedriver.chromium.org/downloads>  

Install Docker, then run

```sh
docker run -p 4444:4444 selenium/standalone-chrome
```
