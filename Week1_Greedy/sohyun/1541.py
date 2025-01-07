arr= input().split('-')

result=[]


for i in arr:
  sum=0
  tmp= i.split('+')
  for j in tmp:
    sum+=int(j)
  result.append(sum)

n= result[0]

for i in range(1, len(result)):
  n-=result[i]

print(n)


