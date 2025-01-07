import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = sorted(list(map(int, input().split())))

sum = (sum(array) - array[-1])/2 + array[-1]
print(sum)

