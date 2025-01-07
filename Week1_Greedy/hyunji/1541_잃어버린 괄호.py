import sys
str = sys.stdin.readline().strip().split("-")
temp = []

for i in str:
    cnt = 0
    for j in i.split("+"):
        cnt += int(j)
    temp.append(cnt)

result = temp[0]
for i in temp[1:]:
    result -= i
print(result)