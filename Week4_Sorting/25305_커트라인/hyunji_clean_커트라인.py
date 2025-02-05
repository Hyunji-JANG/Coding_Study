# 내림차순으로 정렬하지 않고, 오름차순 정렬에서 역순 추출
n,k = map(int, input().split())
scores = map(int, input().split())
print(sorted(scores)[-k])