# 네이버 웹툰 댓글 크롤링
# https://comic.naver.com/webtoon/detail?titleId=834886&no=41&week=mon
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# selenium 객체가 html을 가져온다.
driver.get('https://comic.naver.com/webtoon/detail?titleId=834886&no=41&week=mon')
soup = BeautifulSoup(driver.page_source)

# 댓글창안의 내용을 가져온다.
comment_area = soup.find_all('span', {'class', 'u_cbox_contents'})
print("***********베스트 댓글***********")
for i in range(len(comment_area)):
	comment = comment_area[i].text.strip()
	print(comment)
	print('-' * 30)

time.sleep(10)