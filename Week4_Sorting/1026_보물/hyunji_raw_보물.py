n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = list(map(int, input().split()))
c = [b.index(x) for x in sorted(b)] # b 오름차순 idx
s = 0

for i in range(len(a)):
    s += a[i] * b[c[i]]
print(s)