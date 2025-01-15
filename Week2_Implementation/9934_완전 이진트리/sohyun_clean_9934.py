N = int(input())

inorder = list(map(int, input().split())) # 중위 순회 결과 (노드들이 중위 순서로 정렬된 리스트)

answer= [[] for _ in range(N)] # 각 깊이에 해당하는 노드 값을 저장할 리스트

def dfs(inorder, depth):

  mid = (len(inorder) // 2) # 중간 인덱스 (현재 서브트리의 루트 노드)

  answer[depth].append(inorder[mid]) # 현재 깊이에 해당하는 노드 값 저장

  print('answer',answer)

  if len(inorder) ==1: # 노드가 하나만 남은 경우 재귀 종료
    return
  
  dfs(inorder[:mid],depth+1) # 왼쪽 서브트리 처리
  dfs(inorder[mid+1:],depth+1) # 오른쪽 서브트리 처리

dfs(inorder,0)

for i in answer:
  print(*i)