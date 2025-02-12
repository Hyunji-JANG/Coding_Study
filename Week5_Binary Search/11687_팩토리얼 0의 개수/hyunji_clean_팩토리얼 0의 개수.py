def cnt_zero(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n //= 5
    return cnt


M = int(input())
start = 1
end = M * 5
result = 0

while start <= end:
    mid = (start + end) // 2
    zero = cnt_zero(mid)

    if zero < M:
        start = mid + 1
    else:
        if zero == M:
            result = mid
        end = mid - 1

if result == 0:
    print(-1)
else:
    print(result)