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
- streamlit
- pyperclip

## Included files

- Static  
Includes code that statically crawls stock name, prices and change from Naver and Google.  
Includes code that statically crawls current exchange rate from Naver.  
Simple GUI is made with Streamlit.

- Dynamic  
Uses Selenium for to dynamically crawl Chrome.  
If necessary, download Chromedriver that supports your Chrome version. <https://chromedriver.chromium.org/downloads>  
Please note that using Chromedriver for Selenium has been deprecated, so the step above is no longer necessary.

Install Docker, then run

```sh
docker run -p 4444:4444 selenium/standalone-chrome
```

## Static UI local development

``` sh
python -m streamlit run static/gui.py
```

The UI should be on <http://localhost:8501/>
