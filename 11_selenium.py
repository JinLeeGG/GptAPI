# 야놀자 웹 크롤링
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
	# 리뷰 저장 리스트
	review_list = []
	# chrome driver 하나 만들기 
	driver = webdriver.Chrome()
	# url을 통해서 html 불러오기
	driver.get(url)
	# 2초동안 대기
	time.sleep(2)
	
	scroll_count = 3
	for i in range(scroll_count):
		# 스크롤을 이동시키는 javascript 명령어 (0부터 scrollHeight - 끝까지)
		# javascript문을 넣을 수 있다.
		driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
		# 2초동안 대기
		time.sleep(2)
	
	# 지금까지 내린 상태에서 html을 읽어오고 soup 객체 (파싱가능한 객체) 만들기 
	soup = BeautifulSoup(driver.page_source)
	
	# 전체 리뷰 박스 가져오기
	# 넘버링을 지움으로서 같은 타입의 컨테이너들을 다 가져온다.
	# 번호를 지우면 이 패턴으로 가져오기때문에 비슷한 박스들을 다 가져온다. 
	##__next > section > div > div.css-1js0bc8 > div:nth-child(1) > div:nth-child(2) > div
	review_containers = soup.select("#__next > section > div > div.css-1js0bc8 > div > div > div")
	
	# 리뷰가 적힌 날짜 가져오기
	# #__next > section > div > div.css-1js0bc8 > div:nth-child(1) > div:nth-child(2) > div > div.css-1toaz2b > div:nth-child(1) > div.css-1ivchjf > p
	# 숫자만 뽑아서 공통으로 가져오기 
	review_date = soup.select("#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p")

	# 몇개 나오는지 프린트
	for i in range(len(review_containers)):
		# print(i)
		# 리뷰 내용 가져오기
		review_text = review_containers[i].find("p", class_='content-text').text #class를 찾을때 class_ 사용
		# 리뷰 날짜 가져오기
		date = review_date[i].text
		
		# 리뷰 가져오기
		# print(review_text, date)

		# 리뷰 별점 가져오기
		# 빈 별점 세주기
		review_empty_stars = review_containers[i].find_all('path', {'fill-rule':'evenodd'})
		
		# 최대별 5개에서 빈 별을 빼주면 현재 별점이 나온다.
		stars = 5 - len(review_empty_stars)

		# dict 항목을 3개로 만들기
		review_dict = {
			'review' : review_text,
			'star' : stars,
			'date' : date
		}
		
		# 각 리뷰 항목들을 review_List에다가 추가 
		review_list.append(review_dict)

	# 프린트로 확인
	print(review_list)
	time.sleep(10)


crawl_yanolja_reviews("신라스테이 여수 엑스포역", "https://nol.yanolja.com/reviews/domestic/10046614")

# 요기요 리뷰 크롤링 해보기
# https://ryuzyproject.tistory.com/53