### 다른 풀이
'''
키보드 좌표를 미리 저장해두는 방식
'''
import sys
input = sys.stdin.readline

keyboard = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]

left_keys = "qwertasdfgzxcv"
right_keys = "yuiophjklbnm"

key_pos = {}
for i in range(3):  # 3줄에 걸쳐 키보드 좌표를 저장
    for j in range(len(keyboard[i])):
        key_pos[keyboard[i][j]] = (i, j)
print(key_pos)

sl, sr = input().split()
string = input().strip()

l_pos = key_pos[sl]
r_pos = key_pos[sr]
time = 0

for s in string:
    if s in left_keys:  # 왼손으로 처리해야 하는 키
        next_pos = key_pos[s]
        time += abs(next_pos[0] - l_pos[0]) + abs(next_pos[1] - l_pos[1]) + 1
        l_pos = next_pos  # 왼손의 위치 업데이트
    else:  # 오른손으로 처리해야 하는 키
        next_pos = key_pos[s]
        # 현재 위치에서 새로운 위치까지의 거리 계산
        time += abs(next_pos[0] - r_pos[0]) + abs(next_pos[1] - r_pos[1]) + 1
        r_pos = next_pos  # 오른손의 위치 업데이트

print(time)