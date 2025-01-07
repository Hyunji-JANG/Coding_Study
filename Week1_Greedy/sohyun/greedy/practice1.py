n, m , k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second= data[n-2]

result= 0

count =int(m/(k+1))*k
count += m % (k+1)

result += (count) * first
result += (m-count)* second

print(result)

# 큰 수가 더해지는 횟수
# int(M/(K+1))* K + M % (K+1)