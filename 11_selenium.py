# 야놀자 웹 크롤링
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
	# 리뷰 저장 리스트
	review_list = []
	driver = webdriver.Chrome()
	# url을 통해서 html 불러오기
	driver.get(url)
	time.sleep(2)
	
	scroll_count = 3
	for i in range(scroll_count):
		# 스크롤을 이동시키는 javascript 명령어 (0부터 scrollHeight - 끝까지)
		driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
		time.sleep(2)
	
	# 지금까지 내린 상태에서 html을 뽑기 
	soup = BeautifulSoup(driver.page_source)
	# 넘버링을 지움으로서 같은 타입의 컨테이너들을 다 가져온다.
	##__next > section > div > div.css-1js0bc8 > div:nth-child(1) > div:nth-child(2) > div
	review_containers = soup.select("#__next > section > div > div.css-1js0bc8 > div > div > div")
	
	# 몇개 나오는지 프린트
	for i in range(len(review_containers)):
		print(i)

	time.sleep(10)


crawl_yanolja_reviews("신라스테이 여수 엑스포역", "https://nol.yanolja.com/reviews/domestic/10046614")