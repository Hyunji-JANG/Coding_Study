n = int(input())
ref = list(map(int, input().split()))
ref.sort()      # 오름차순 정렬
max = ref[-1]   # 인용 횟수중 가장 큰 수
q = 0           # q 인덱스

for k in reversed(range(1, max)):   # max-1 ~ 1
    tmp = list(filter(lambda x: x >= k, ref))   # k번 이상 인용된 횟수 리스트
    if len(tmp) >= k:   # k번 이상 인용된 횟수가 k번 이상
        q = k
        break
print(q)