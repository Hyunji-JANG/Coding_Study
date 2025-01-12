import sys
input = sys.stdin.readline

n = int(input())    # 파일 개수
f_list = [[] for _ in range(n)]     # 입력 값을 위한 리스트
for i in range(n):                  # 입력 값을 파일명-확장자명 구분해서 리스트에 저장
    f_list[i] = input().strip().split(".")

extension_list = []                 # 확장자 명만 저장하는 리스트
for f in f_list:                    # 리스트에 확장자명 저장
    extension_list.append(f[1])
extension_list.sort()               # 오름차순으로 sort

f_dict = {}                         # 확장자명 딕셔너리
for i in extension_list:
    if i not in f_dict:             # 해당 확장자가 딕셔너리에 없으면
        f_dict[i] = 1               # 딕셔너리에 추가, count = 1
    else:                           # 해당 확장자가 딕셔너리에 았으면
        f_dict[i] += 1              # count만 1 추가

for ele in f_dict:
    print(ele, f_dict[ele])
