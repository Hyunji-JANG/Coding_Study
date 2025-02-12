N = int(input())

array1 = set(map(int, input().split()))

M = int(input())

array2 = list(map(int, input().split()))

array3= []

for i in range(len(array2)):
  if array2[i] in array1:
    array3.append(1)
  else:
    array3.append(0)

for i in range(len(array3)):
  print(array3[i], end= " ")