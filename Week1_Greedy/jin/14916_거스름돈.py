n = int(input())
count = -1

m = n // 5

for i in range(m, -1, -1):
	if (n - i * 5) % 2 == 1:
		continue
	elif (n - i * 5) % 2 == 0:
		count = 0
		count += i
		count += (n - i * 5) // 2
		break

print(count)