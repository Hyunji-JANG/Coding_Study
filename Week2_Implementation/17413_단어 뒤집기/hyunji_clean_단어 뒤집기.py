### 간결한 풀이 1
def reverse_word(word):
    result = []
    split_by_tag = word.split('<')          # < 까지 끊음
    for n in split_by_tag:
        if '>' in n:                        # 태그의 끝(>)을 포함하고 있다면
            tag, rest = n.split('>', 1)     # tag에 > 전까지, rest에 > 후부터 저장
            result.append(f'<{tag}>')       # 리스트에 <> 형식으로 추가
            reversed_rest = ' '.join(m[::-1] for m in rest.split())     # > 후부터 공백으로 슬라이싱한 뒤 역순으로 문자열 만들기
            result.append(reversed_rest)    # 문자열을 리스트에 추가
        else:                               # 태그를 포함하지 않는 경우
            just_word = ' '.join(i[::-1] for i in n.split())    # 공백으로 슬라이싱한 뒤 역순으로 문자열 만들기
            result.append(just_word)        # 문자열을 리스트에 추가

    answer = ''.join(result)                # join() 함수로 문자열 생성
    return answer

word = input()
print(reverse_word(word))

### 간결한 풀이 2
'''
stack을 사용하는 방법
'''

import sys
str = sys.stdin.readline().strip() + ' '    # 마지막에 공백 더해주기
stack = []                                  # 저장할 스택
result = ''                                 # 결과물 출력
cnt = False                                 # 태그 안에 있는지 여부

for i in str:
    if i == '<':                        # '<'를 만나면
        cnt = True                      # 현재 괄호 안에 있음을 표시
        for _ in range(len(stack)):     # 괄호 만나기 이전 stack 비워주고 다 더함
            result += stack.pop()
    stack.append(i)

    if i == '>':                        # '<'를 만나면
        cnt = False                     # 지금 괄호를 빠져 나왔음을 표시
        for _ in range(len(stack)):     # <> 안에 있으므로 뒤집지 않고 더함
            result += stack.pop(0)

    if i == ' ' and cnt == 0:           # 공백을 만나고 괄호 밖이라면
        stack.pop()                     # 공백 빼주기
        for _ in range(len(stack)):     # 뒤집어서 더해주기
            result += stack.pop()
        result += ' '                   # 마지막에 공백 살려주기

print(result)
