import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]
dp = [0] * n                    # 최댓값

if n <= 2:
    print(sum(step))
else:
    dp[0] = step[0]             # 첫 번째 계단
    dp[1] = step[0] + step[1]   # 첫 번째 + 두 번째 계단
    dp[2] = max(step[0] + step[2], step[1] + step[2])   # 1,3번 vs. 2,3번
    for i in range(3, n):
        # (i-3)까지와 i, i-1번 연속 vs (i-2)까지와 i번
        dp[i] = max((dp[i-3] + step[i] + step[i-1]), (dp[i-2] + step[i]))
print(dp[n-1])