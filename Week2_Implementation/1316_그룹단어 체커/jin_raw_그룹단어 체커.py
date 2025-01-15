N = int(input())
groups = 0

for i in range(N):
    word = input()
    seen = set()
    is_group_word = True
    previous_char = None

    for char in word:
        if char in seen:
              # 이전 문자와 현재 문자가 다르면서 이미 나온 적이 있다면 그룹 단어가 아님
            if char != previous_char:
                is_group_word = False
                break
        else:
            seen.add(char)
        # 현재 문자를 이전 문자로 업데이트
        previous_char = char

    if is_group_word:
        groups += 1

print(groups)