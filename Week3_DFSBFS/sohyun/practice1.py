from collections import deque
# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자류구조를 활용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력