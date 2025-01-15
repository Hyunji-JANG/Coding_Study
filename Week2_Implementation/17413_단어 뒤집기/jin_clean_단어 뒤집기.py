S = input().strip()

result = []
i = 0
while i < len(S):
	# 태그인 부분
	if S[i] == '<':
	# find 함수: 문자열에서 찾고자 하는 문자열의 위치 인덱스 값을 정수로 반환
		j = S.find('>', i) + 1
		# 태그를 결과에 추가
		result.append(S[i:j])
		i = j
	# 태그가 아닌 부분
	else:
		# 태그가 끝나는 부분
		j = i
		# 다음 태그 시작이나 문자열 끝까지 이동
		while j < len(S) and S[j] != '<':
			j += 1
		# 공백을 기준으로 단어 분리
		words = S[i:j].split()
		# 각 단어를 뒤집고 다시 조합
		reversed_words = ' '.join(word[::-1] for word in words)
		result.append(reversed_words)
		i = j

print(''.join(result))