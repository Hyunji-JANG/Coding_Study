N , K = map(int, input().split())

count=0

while True:
  # n==k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
  target = (N//K)*K
  count += (N-target)
  N= target
  #n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출 
  if N<K:
    break
  count+=1
  N//=K

#마지막으로 남은 수에 대하여 1씩 빼기
count+=(N-1)
print(count) 
