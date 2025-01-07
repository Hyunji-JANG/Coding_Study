import sys
input = sys.stdin.readline

n = int(input())
cost = [int(input()) for _ in range(n)]
cost.sort(reverse = True)

for i in range(2, n, 3):
    cost[i] = 0
print(sum(cost))
