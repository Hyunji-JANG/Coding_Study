# remove 사용
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
s = 0
for i in range(n):
    b_max = max(b)
    s += a[i] * b_max
    b.remove(b_max)

# pop 사용
for i in a:
    b_max = max(b)
    b.pop(b.index(b_max))
    s += i * b_max