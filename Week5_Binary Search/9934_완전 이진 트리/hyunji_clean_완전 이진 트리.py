import sys
input = sys.stdin.readline

K  = int(input())
seq = list(map(int, input().split()))

tree = [[] for _ in range(K)]

def binary_tree(start, end, depth):
    if start > end:
        return
    mid = (start + end) // 2
    tree[depth].append(seq[mid])
    binary_tree(start, mid - 1, depth + 1)
    binary_tree(mid + 1, end, depth + 1)

binary_tree(0, len(seq)-1, 0)
for t in tree:
    print(*t)