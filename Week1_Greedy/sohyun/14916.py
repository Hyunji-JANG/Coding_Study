coin = int(input())
count = 0

while coin > 0:
  if coin % 5 == 0:
    count += 1
    coin -= 5
  else:
    coin -= 2
    count += 1

if coin < 0:
  print(-1)
else:
  print(count)
