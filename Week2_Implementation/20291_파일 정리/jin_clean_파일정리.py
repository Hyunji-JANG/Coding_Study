from sys import stdin

# key가 파일 확장자이고 value는 해당 확장자의 파일 수인 result 딕셔너리 생성
result = {}

# 표준 입력으로부터 모든 줄을 읽어와서 리스트로 반환
# 첫번째 줄은 파일 수이므로 제외
for line in stdin.readlines()[1:]:
    # 각 줄 양쪽 끝에서 공백 문자 또는 줄바꿈 문자 제외
    # key에 확장자 이름을 저장
    key = line.strip().split(".")[1]
    # 딕셔너리 result에서 key에 해당하는 값을 가져옴
    # 값이 없으면 0을 반환
    # 해당 확장자의 값을 1 증가
    result[key] = result.get(key, 0) + 1

# 딕셔너리의 모든 key를 가져와서 사전순으로 정렬
# 각 확장자와 파일 수를 문자열로 출력
print("\n".join(f"{re} {result[re]}" for re in sorted(list(result.keys()))))