import sys

input = sys.stdin.readline
n = int(input())
words = list(set(input().strip() for _ in range(n)))
words.sort()    # 단어 오름차순 먼저 정렬
print('\n'.join(sorted(words, key=len)))    # len으로 재정렬