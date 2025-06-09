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

# 베스트 댓글을 크롤링한다. 
print("***********베스트 댓글***********")
for i in range(len(comment_area)):
	comment = comment_area[i].text.strip()
	print(comment)
	print('-' * 30)


'''
※ xpath

XPath는 XML 또는 HTML 문서 내에서 특정 요소나 속성을 선택하기 위해 사용되는 경로 표현 언어입니다. 웹 크롤링이나 자동화 도구에서 주로 사용되며, 요소를 효율적으로 찾을 수 있도록 도와줍니다. 일반적인 XPath는 특정 위치나 속성을 기준으로 요소를 선택하는 상대적인 경로를 사용합니다. 또한 full xpath는 루트 요소에서 시작하여 대상 요소까지의 절대적인 경로를 나타냅니다. 따라서 문서 구조가 변경되면 경로가 깨질 가능성이 높습니다.
'''
# 전체댓글 xpath: /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]

# xpath로 찾아서 전체댓글 클릭
driver.find_element('xpath', '/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]').click()

# 2초 기다리기 (인터넷 로드 시간)
time.sleep(2)

# soup 안에 내용을 다시 넣는다.
soup = BeautifulSoup(driver.page_source)
# 댓글창안의 내용을 가져온다.
comment_area = soup.find_all('span', {'class', 'u_cbox_contents'})

# 전체 댓글을 크롤링한다. 
print()
print("***********전체 댓글***********")
for i in range(len(comment_area)):
	comment = comment_area[i].text.strip()
	print(comment)
	print('-' * 30)

# 10초 기다리기
time.sleep(30)