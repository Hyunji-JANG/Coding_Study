change = int(input())
count = 0

if change == 1 or change == 3:
    print("-1")
else:
    count = change // 5
    change %= 5
    if change % 2 == 1:
        count -= 1
        change += 5
    print(count + change // 2)
