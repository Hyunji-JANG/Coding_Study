import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = sorted(list(map(int, input().split())))
print(data[k-1])