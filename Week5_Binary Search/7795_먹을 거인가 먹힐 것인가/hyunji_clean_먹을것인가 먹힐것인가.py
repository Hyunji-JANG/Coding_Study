import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans = 0
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    cnt = 0
    pair = 0

    for i in range(N):
        while True:
            # a[i]가 b의 모든 원소보다 큰 경우
            # a[i]가 b[cnt] 보다 작아서 b의 뒤 원소들을 살펴볼 필요가 없을 때
            if cnt == M or a[i] <= b[cnt]:
                pair += cnt
                break
            else:
                cnt += 1
    print(pair)