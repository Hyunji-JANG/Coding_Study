input_str = list(input())

cnt = 0
cnt_list = []
for s in input_str:
	if s == 'X':
		cnt += 1
	elif s == '.':
		if cnt > 0:
			cnt_list.append(cnt)
			cnt = 0
		cnt_list.append(0)
if cnt > 0:
	cnt_list.append(cnt)

result = ""
for c in cnt_list:
	if c == 0:
		result += "."
	elif c % 4 == 0:
		result += "AAAA" * (c // 4)
	elif c % 2 == 0:
		result += "AAAA" * (c // 4) + "BB"
	else:
		result = -1
		break

if result == -1:
    print(-1)
else:
    print(result)