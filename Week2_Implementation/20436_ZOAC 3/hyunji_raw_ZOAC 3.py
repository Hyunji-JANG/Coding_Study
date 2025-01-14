sl, sr = input().split()
str = input()

left = [['q','w','e','r','t'], ['a','s','d','f','g'], ['z','x','c','v']]
right = [['','y','u','i','o','p'], ['','h','j','k','l'], ['b','n','m']]
cnt = len(str)

l_temp = [0,0]
r_temp = [0,0]

for row, r in enumerate(left):
    if sl in r:
        l_temp = [row, r.index(sl)]
for row, r in enumerate(right):
    if sr in r:
        r_temp = [row, r.index(sr)]

for s in str:
    # 왼손 반복
    for row, r in enumerate(left):
        if s in r:  # left[i]에 알파벳 있으면
            temp = [row, r.index(s)]
            time_move = abs(l_temp[0] - temp[0]) + abs(l_temp[1] - temp[1])
            cnt += time_move
            l_temp = temp

    # 오른손 반복
    for row, r in enumerate(right):
        if s in r:  # left[i]에 알파벳 있으면
            temp = [row, r.index(s)]
            time_move = abs(r_temp[0] - temp[0]) + abs(r_temp[1] - temp[1])
            cnt += time_move
            r_temp = temp
