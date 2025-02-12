import bisect

n = int(input())
n_arr = sorted(list(map(int, input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    l = bisect.bisect_left(n_arr, i)
    r = bisect.bisect_right(n_arr, i)
    print(r-l, end=' ')