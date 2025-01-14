import sys
import copy
input = sys.stdin.readline

def turn45(before, after):
    for i in range(n):
        after[i][i] = before[n//2][i]           # \
        after[i][n//2] = before[i][i]           # |
        after[i][n-1-i] = before[i][n//2]       # /
        after[n//2][n-1-i] = before[i][n-1-i]   # -

T = int(input().rstrip())
for _ in range(T):
    n,d = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    print(board)

    if d < 0:
        d = (d + 360) % 360

    cnt = d // 45
    res = copy.deepcopy(board)

    for _ in range(cnt):
        turn45(board, res)
        board = copy.deepcopy(res)

    for line in res:
        print(*line)