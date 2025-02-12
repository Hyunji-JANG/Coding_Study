import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

input = sys.stdin.readline
n = int(input())
n_arr = sorted(list(map(int, input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

for idx, i in enumerate(m_arr):
    m_arr[idx] = binary_search(n_arr, i, 0, n-1)

print(*m_arr)
