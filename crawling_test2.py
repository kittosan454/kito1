from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
import multiprocessing
from multiprocessing.pool import Pool, ThreadPool
import threading

options = webdriver.ChromeOptions()
# options.add_argument('headless') # 웹브라우저가 안뜬다.
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,  'app_banner': 2, 'protocol_handlers': 2, 'plugins': 2, 'popups': 2
                                                    ,'geolocation': 2,'site_engagement': 2, 'mouselock': 2, 'metro_switch_to_desktop': 2,
                                                    'auto_select_certificate': 2, 'fullscreen': 2, 'mixed_script': 2, 'media_stream': 2,
                                                    'media_stream_mic': 2, 'media_stream_camera': 2, 'ppapi_broker': 2, 'midi_sysex': 2,
                                                    'push_messaging': 2, 'ssl_cert_decisions': 2, 'durable_storage': 2,
                                                    'protected_media_identifier': 2,  'automatic_downloads': 2, 'notifications': 2,}}
#


#
# app banner 페이지에서 뜨는 배너 삭제, 자바 스크립트 실행 없음(복 붙 허용), 쿠키 금지
options.add_argument('headless')
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('window-size=1920x1080') # 웹브라우저 크기 고정
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument('lang=ko_KR') # 한국어를 써야 그대로 나옴
options.add_argument('disable_gpu')

driver = webdriver.Chrome('./chromedriver', options=options)



# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020
# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=1
# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=2 37까지

# //*[@id="old_content"]/ul/li[1]/a
# //*[@id="old_content"]/ul/li[2]/a
# //*[@id="old_content"]/ul/li[20]/a
# //*[@id="movieEndTabMenu"]/li[6]/a/em # 리뷰 버튼
#
# //*[@id="reviewTab"]/div/div/div[2]/span/em # 리뷰 개수
# //*[@id="reviewTab"]/div/div/ul/li[1]/a/strong 리뷰 제목
# //*[@id="pagerTagAnchor1"] 리뷰 페이지 버튼
# //*[@id="pagerTagAnchor2"]
# //*[@id="content"]/div[1]/div[4]/div[1]/div[4]/div # class="user_tx_area"
start_time = time.time()
review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a'
review_number_xpath = '//*[@id="reviewTab"]/div/div/div[2]/span/em'
# review_button_xpath_5='//*[@id="movieEndTabMenu"]/li[5]/a'

case = [20, 21]
def getCase(case):
    try:
        url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2017&page=' +str(case)

        titles = []
        reviews = []

        for j in range(1, 21):
            try:
                driver.get(url)
                movie_title_xpath ='//*[@id="old_content"]/ul/li[{}]/a'.format(j) # 영화 타이틀을 받아온다.
                title = driver.find_element_by_xpath(movie_title_xpath).text # 텍스트 파일 저장


                driver.find_element_by_xpath(movie_title_xpath).click()
                # driver.find_element_by_xpath(review_button_xpath).click() # 클릭은 믿을게 못된다.

                review_page_url = driver.find_element_by_xpath(review_button_xpath).get_attribute('href')  # href속성값을 가져온다. 주소다

                driver.get(review_page_url) #확실한건 driver get 속성값의 드라이버를 받아온다.
                review_range = driver.find_element_by_xpath(review_number_xpath).text.replace(',', '')
                 # 1000이 넘어가는 것중에 콤마를 뺌
                review_range = int(review_range)
                review_range = review_range // 10 + 2
                if review_range > 6:
                    review_range =6

                for k in range(1, review_range):

                    driver.get(review_page_url + '&page={}'.format(k)) # 페이지를 이어 붙여준다.
                    # time.sleep(0.3)
                    for l in range(1, 11):
                        review_title_xpath= '//*[@id="reviewTab"]/div/div/ul/li[{}]/a/strong'.format(l)
                        try:
                            driver.find_element_by_xpath(review_title_xpath).click()
                            # time.sleep(0.3)
                            time.sleep(0.3)
                            review = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div[4]').text
                            # print('========================= ==================')
                            # print(title)
                            # print(review)
                            titles.append(title)
                            reviews.append(review)
                            driver.back()
                        except:
                            print(l, '번째 review가 없다.')
                            # driver.get(url)
                            break
            except:
                print('error')

        df_review_20 = pd.DataFrame({'title': titles, 'reviews': reviews}) # 20 개씩저장
        df_review_20.to_csv('./crawling_data/reviews_test_{}.csv'.format(case), index=False)
    except:
        print('totally error')
    finally:
        driver.close()

    df_review_20.info()
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    pool.map(getCase, case) # getcase 에 case인자 전달
    pool.close() # 리소스 낭비를 위한 close
    pool.join() # 작업 완료 대기를 위한 join


print("실행 시간 : %s초" % (time.time() - start_time))

# df_review = pd.DataFrame({'title':titles, 'reviews':reviews})
#