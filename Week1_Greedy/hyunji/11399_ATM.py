n = int(input())
array = sorted(list(map(int, input().split())))
time_array = []
sum = 0

for i in range(n):
    for j in range(i+1):
        sum += int(array[j])
    time_array.append(sum)
print(max(time_array))
