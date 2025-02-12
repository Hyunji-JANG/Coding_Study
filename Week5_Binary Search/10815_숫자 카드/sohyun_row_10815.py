N = int(input())

array1= list(map(int, input().split()))

M = int(input())

array2 = list(map(int, input().split()))

array3= []

for i in range(len(array2)):
  if array2[i] in array1:
    array3.append(1)
  else:
    array3.append(0)

print(array3)

##########

N = int(input())

array1= list(map(int, input().split()))

M = int(input())

array2 = list(map(int, input().split()))

array3 = [1 if num in array1 else 0 for num in array2]

print(array3)