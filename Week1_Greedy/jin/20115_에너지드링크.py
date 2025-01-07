N = int(input())
drinks = list(map(int, input().split()))

drinks.sort()

for i in range(N-1):
	new_drink = drinks[-1] + drinks[0] / 2
	drinks.pop(0)
	drinks.pop(len(drinks)-1)
	drinks.append(new_drink)

print(drinks[0])