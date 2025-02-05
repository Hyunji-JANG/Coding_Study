n = int(input())
data = list(set(input() for _ in range(n)))
res = sorted(data, key=lambda x:(len(x), x))    # len으로 먼저 정렬 후 단어 오름차순 정렬
print('\n'.join(res))