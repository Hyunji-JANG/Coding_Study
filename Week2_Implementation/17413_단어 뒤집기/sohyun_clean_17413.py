import sys
input = sys.stdin.readline
l = list(input().rstrip())

res = []
flag = False
tmp = ''

for i in range(len(l)):
    if l[i] == '<':
        if tmp not in '':
            res.append(tmp[::-1])
            tmp = ''
        res.append(l[i])
        flag = True
        continue

    if l[i] == '>':
        res.append(l[i])
        flag = False
        continue

    if flag:
        res.append(l[i])
        continue

    if l[i] == ' ':
        res.append(tmp[::-1] + l[i])
        tmp = ''
        continue

    if i == len(l) - 1:
        tmp += l[i]
        res.append(tmp[::-1])
        break

    tmp += l[i]

print(''.join(res))
