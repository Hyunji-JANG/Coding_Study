N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
	a, b = map(int, input().split(' '))
	graph[a].append(b)
	graph[b].append(a)

def dfs(graph, v, visited):
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

visited = [False] * (N+1)

# 노드 1에서 탐색 시작
dfs(graph, 1, visited)

cnt = 0
for i in range(2, N+1): # 1번 컴퓨터를 제외하고 카운트
	if visited[i]:
		cnt += 1
print(cnt)