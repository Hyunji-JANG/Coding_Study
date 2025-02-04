N= int(input())

array= []

for i in range(N):
  coordinate= list(map(int,input().split()))
  array.append(coordinate)


result= sorted(array, key=lambda x: (x[1], x[0]))

for i in range(N):
  print(result[i][0], result[i][1])