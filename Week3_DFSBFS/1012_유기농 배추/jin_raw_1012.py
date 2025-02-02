# 재귀 깊이 제한을 늘리기
import sys

sys.setrecursionlimit(10**6)

T = int(input())

def dfs(x, y):
	if x < 0 or y < 0 or x >= N or y >=M:
		return False
	if graph[x][y] == 1:
		# graph에서 이미 방문한 곳을 0으로 처리
		graph[x][y] = 0
		dfs(x-1, y)
		dfs(x, y-1)
		dfs(x+1, y)
		dfs(x, y+1)
		return True
	return False

result = []
for i in range(T):
	M, N, K = map(int, input().split(' '))
	graph = [[0]*(M) for _ in range(N)]
	for j in range(K):
		x, y = map(int, input().split(' '))
		graph[y][x] = 1
	# DFS 수행하며 배추흰지렁이 수 구하기
	cnt = 0
	for m in range(M):
		for n in range(N):
			if dfs(n, m):
				cnt += 1
	result.append(cnt)

for p in range(T):
	print(result[p])