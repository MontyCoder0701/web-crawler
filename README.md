# Web-crawler

Web crawler made with Python.  
For both static and dynamic crawling.  

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Virtual environment setup

Create venv

```sh
py -m venv env
```

Run venv

```sh
.\env\Scripts\activate.ps1
```

If there is unrestricted access problems,

```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

## Used libraries

- requests
- beautifulsoup4
- selenium
- streamlit
- pyperclip

## Installing libraries

```sh
py -m pip install [library-name]
```

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
py -m streamlit run static/gui.py
```

![image](https://user-images.githubusercontent.com/104475739/208848737-ccc592a9-d8cf-46f7-8385-8b32b9c9fcb5.png)

The UI should be on <http://localhost:8501/>
