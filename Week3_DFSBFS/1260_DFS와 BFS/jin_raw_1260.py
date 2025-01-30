from collections import deque

N, M, V = map(int, input().split(' '))

graph = [[] for _ in range(N+1)]

for i in range(M):
	a, b = map(int, input().split(' '))
	graph[a].append(b)
	graph[b].append(a)

for i in range(N+1):
	graph[i].sort()
	
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

track_dfs = []
track_bfs = []

def dfs(graph, v, visited, track):
	visited[v] = True
	track.append(v)
	for node in graph[v]:
		if not visited[node]:
			dfs(graph, node, visited, track)

def bfs(graph, start, visited, track):
	queue = deque([start])
	visited[start] = True
	while queue:
		v = queue.popleft()
		track.append(v)
		for node in graph[v]:
			if not visited[node]:
				queue.append(node)
				visited[node] = True

dfs(graph, V, visited1, track_dfs)
bfs(graph, V, visited2, track_bfs)

for i in range(len(track_dfs)):
	print(track_dfs[i], end=' ')
print('')
for j in range(len(track_bfs)):
	print(track_bfs[j], end=' ')