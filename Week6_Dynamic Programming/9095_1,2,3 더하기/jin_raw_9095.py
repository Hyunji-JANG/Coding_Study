T = int(input())
t = []

for i in range(T):
	t.append(int(input()))

def dp(num):
	if num == 1:
		return 1
	elif num == 2:
		return 2
	elif num == 3:
		return 4
	else:
		d = [0] * num
		d[0] = 1
		d[1] = 2
		d[2] = 4
		for j in range(3, num):
			d[j] = d[j-1] + d[j-2] + d[j-3]
		return d[(num-1)]

for i in t:
	print(dp(i))