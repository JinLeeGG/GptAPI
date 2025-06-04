from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chrome 창이 실행되었다 없어진다.
driver = webdriver.Chrome()
# 이 사이트로 이동
driver.get('https://www.google.com')
# name이 q인것을 찾아라
search = driver.find_element('name', 'q')
# search 칸에다가 '날씨' 라고 입력
search.send_keys('날씨')
# enter키
search.send_keys(Keys.RETURN)

time.sleep(10)

