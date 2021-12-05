# 2019.07.20-KimSeokMin
# 필요 라이브러리 : selenium, bs4(beautifulsoup)
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as BS
from multiprocessing.pool import Pool, ThreadPool
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
import threading
import re
import csv

casenum = 1

# def getCaseNum(html):
#     global casenum # casenum을 글로벌 변수로 정의한다.
#     bs = BS(html, "lxml") #
#     csnum = bs.find_all("a", {"class": "layer_pop_open"})
#     arr = [] # 빈리스트 하나를 만든다.
#     for i in csnum: # 받아온 값에 대하여
#         cs = i.get('id') # id를 받는다. 문자열로 받는듯
#         cs = cs.replace("py_", "") # 받은 id에서 py_를 지우고 숫자만 받아옴
#         arr += [[casenum, int(cs)]] # 리스트로 받는다.
#         print(casenum, cs)
#         casenum += 1 # case 넘버 1씩 증가시켜간다.
#     return arr
bs = BS('https://glaw.scourt.go.kr/wsjo/panre/sjo050.do#//', "lxml")
print(bs)
csnum = bs.find_all("a", {"class": "layer_pop_open"})
print(csnum)
arr = [] # 빈리스트 하나를 만든다.