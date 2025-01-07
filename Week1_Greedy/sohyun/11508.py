N= int(input())
arr = [int(input()) for _ in range(N)]

arr.sort(reverse=True)

result=0

for i in range(N):
  if i%3 ==2:
    continue
  result+=arr[i]

print(result)
