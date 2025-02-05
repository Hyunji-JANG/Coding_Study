n = int(input())

array = []
for i in range(n):
    x,y = map(int, input().split())
    array.append((y, x))    # y 좌표로 sorting하기 위해 먼저 저장

array.sort()    # y 좌표 기준으로 오름차순 정렬

for y,x in array:
    print(x, y) # x 좌표 먼저 출력