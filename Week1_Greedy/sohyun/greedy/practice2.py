N, M = map(int, input().split())

arr= [list(map(int, input().split())) for _ in range(N)]


min_arr= []
for i in range(N):
  min_arr.append(min(arr[i]))

print(max(min_arr))