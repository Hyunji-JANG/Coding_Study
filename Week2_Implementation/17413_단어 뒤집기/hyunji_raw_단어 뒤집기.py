def getTagIndex(arr):
    if '<' in arr:      # 태그가 있으면 -> 태그의 [start], [end] 반환
        start = arr.index('<')
        end = arr.index('>') + 1
    else:               # 태그가 없으면 -> 리스트의 마지막 인덱스 반환
        start = end = -1
    return start, end

import sys
raw = list(sys.stdin.readline().rstrip())
origin_len= len(raw)

words = []
while True:
    start, end = getTagIndex(raw)
    last = end

    if start == -1:
        temp = "".join(raw)
        words.append(temp.split(" "))
        break
    elif start not in [-1, 0]:  # 태그가 있고, 시작이 아닐 때
        temp = "".join(raw[:start])
        words.append(temp.split(" "))
        raw = raw[start:]
    else:
        words.append("".join(raw[start:end]))
        if end == len(raw):
            break
        else:
            raw = raw[end:]

    # 문자열 끝이면 loop 종료
    if end+1 == origin_len:
        break

print("words: ", words)

for word in words:
    if '<' in word:
        print(word, end='')
    else:
        for i in range(len(word)-1):
            print(word[i][::-1], end=' ')
        print(word[-1][::-1], end='')