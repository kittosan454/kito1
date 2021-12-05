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

path = "./chromedriver"
url = "https://glaw.scourt.go.kr/wsjo/panre/sjo050.do"
url2 = "https://glaw.scourt.go.kr/wsjo/panre/sjo100.do?contId="
threadLocal = threading.local() # thread local 즉 스레드 로컬영역을 만든다.



def get_driver():
    driver = getattr(threadLocal, 'driver', None) # 객체인 threadlocal 속성을 가진 driver 속성값 부여 초기화
    if driver is None:
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2}}
        options.add_argument('headless')
        options.add_experimental_option('prefs', prefs)
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        driver = webdriver.Chrome(path, chrome_options=options)
        setattr(threadLocal, 'driver', driver) # 객체에 새로운 속성을 부여함 threadlocal.driver=> driver 값으로 하게함
    return driver



driver = get_driver() # 세팅된 드라이버를 받는다.
    link = url2 + str(case[1]) # url2에 문자열 case[1](판례번호) 을 붙여 link로 받는다.
    driver.get(link) # 웹페이지 연다


bs = BS(html, "lxml")
csnum = bs.find_all("a", {"class": "layer_pop_open"})
arr = []
for i in csnum:
    cs = i.get('id')
    cs = cs.replace("py_", "")
    arr += [[casenum, int(cs)]]
    print(casenum, cs)
    casenum += 1