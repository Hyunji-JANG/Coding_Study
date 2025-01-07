N = int(input())
prices = []
for i in range(N):
	prices.append(int(input()))

prices.sort()

total = 0
for i in range(N):
	if (i + 1) % 3 != 0:
		total += prices[N - 1 - i]

print(total)