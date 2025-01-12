### clean 풀이 1
'''
collections 모듈의 Counter 함수 사용
Counter는 딕셔너리처럼 사용이 가능함
(dictionary는 key 값을 정렬하지 못하는 점도 해결 가능)
인사이트) 입력값의 [0]번 (즉, 파일 명)은 필요없기 때문에 저장하지 않음
'''
import sys
from collections import Counter

data = sys.stdin.read().splitlines()    # 입력 한 번에 받기
n = int(data[0])                        # 첫 번째 줄 - 파일 개수

extensions = [file_name.split('.')[-1] for file_name in data[1:]]   # 확장자 추출 후 저장
extensions_counts = Counter(extensions)                             # 확장자 개수별로 세기
print("\n".join(f"{key} {extensions_counts[key]}" for key in sorted(extensions_counts)))

### clean 풀이 2
'''
Counter 대신 딕셔너리 사용하는 방법
딕셔너리가 key 값을 정렬하지 못하는 방법 -> .keys()를 list로 변환 후 sorted() 함수에 적용
* 문법
사전형데이터.get(키, 디폴트값)
'''
from sys import stdin

result = {}
for line in stdin.readlines()[1:]:
    key = line.strip().split(".")[1]
    result[key] = result.get(key, 0) + 1
print("\n".join(f"{key} {result[key]}" for key in sorted(list(result.keys()))))