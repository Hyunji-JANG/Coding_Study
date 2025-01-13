n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    print(list(word))
    print(sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)