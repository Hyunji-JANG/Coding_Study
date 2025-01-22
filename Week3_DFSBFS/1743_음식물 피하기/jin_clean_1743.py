from collections import deque

N, M, K = map(int, input().split(' '))

graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for i in range(K):
	x, y = map(int, input().split(' '))
	graph[x-1][y-1] = 1
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

length = []

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	visited[x][y] = True
	area_size = 1
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < M:
				if graph[nx][ny] == 1 and not visited[nx][ny]:
					visited[nx][ny] = True
					queue.append((nx, ny))
					area_size += 1
	return area_size

max_size = 0
for i in range(N):
	for j in range(M):
		if graph[i][j] == 1 and not visited[i][j]:
			max_size = max(max_size, bfs(i, j))

print(max_size)