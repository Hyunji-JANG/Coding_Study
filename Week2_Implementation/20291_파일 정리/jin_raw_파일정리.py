N = int(input())
# ext_count 딕셔너리에 확장자를 key, 확장자가 나온 횟수를 value로 하여 저장
ext_count = {}

for i in range(N):
	# 확장자를 분리하여 ext에 저장
	ext = input().split('.')[1]
	if ext in ext_count:
		ext_count[ext] += 1
	else:
		ext_count[ext] = 1

# 확장자 이름을 기준으로 정렬
sorted_ext = sorted(ext_count.keys())

for ext in sorted_ext:
	print(f"{ext} {ext_count[ext]}")