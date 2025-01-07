n = int(input())
p_list = list(map(int, input().split()))

p_list.sort()

total_time = 0
for idx in range(len(p_list)):
	time = 0
	for i in range(idx+1):
		time += p_list[i]
	total_time += time

print(total_time)