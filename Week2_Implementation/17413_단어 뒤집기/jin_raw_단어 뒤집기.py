# 정규표현식
import re

S = input()
splitted = re.split(r'([<>])', S) # 구분자를 포함하여 분리 후 리스트 생성

result = ""
idx = 0
while idx < len(splitted):
  # 태그일 경우
	if splitted[idx] == '<':
		tag = splitted[idx] + splitted[idx+1] + splitted[idx+2]
		result += tag # 태그를 result 문자열에 합치기
		idx += 3
  # 태그가 아닐 경우
	else:
    # 공백을 기준으로 단어들을 분리
		word_chunks = re.split(r'([\s])', splitted[idx])
    # 분리한 단어들을 뒤집기
		for word in word_chunks:
			reverted = ""
			for i in range(1, len(word)+1):
				reverted += word[len(word)-i]
			result += reverted # 뒤집은 단어들을 result 문자열에 합치기
		idx += 1
print(result)