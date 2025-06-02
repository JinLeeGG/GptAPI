import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
	api_key= os.getenv("API_KEY")
)

# temperature: 출력의 무작위성(창의성), 0.0 <= x < 1.0
# 값이 낮을수록 결정론적, 높을수록 무작위성
# 0.0 항상 같은 입력 -> 같은 출력 (답, 수학, 정답형 질문)
# 0.x: 정당한 무작위성 (마케팅 문구, 스토리 작성)

response = client.chat.completions.create(
	model = "gpt-4.1-2025-04-14",
	messages = [
		{"role" : "user", "content" : "왜 강남은 강남이라고 할까요?"}
	],
	temperature = 0.0 
)

# print(response)

#한글만 가져오기
print(response.choices[0].message.content)