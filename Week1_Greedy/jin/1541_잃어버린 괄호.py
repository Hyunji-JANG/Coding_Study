input_str = input()

splitted = input_str.split('-')

num_list = []

for string in splitted:
	if '+' in string:
		mid = 0
		plus_str = string.split('+')
		for n in plus_str:
			mid += int(n)
		# mid = 90
		num_list.append(mid)
	else:
		num_list.append(int(string))

if len(num_list) == 1:
	print(num_list[0])
else:
	result = num_list[0]
	for i in range(1,len(num_list)):
		result -= num_list[i]
	print(result)