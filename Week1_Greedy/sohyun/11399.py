N= int(input())
arr = list(map(int, input().split()))

result=0

arr.sort()


for i in range(1,N):
  arr[i] += arr[i-1]

for i in range(N):
  result+= arr[i]

print(result)