n = int(input())
ref = sorted(list(map(int, input().split())))

def getQ(n):
    res = 0
    for k in range(1, n+1):
        temp, c = 0, 0
        for j in ref:   # j - 인용 횟수
            if j >= k:  # k번 이상 인용된 횟수 카운팅
                temp += 1
            if j <= k:  # k번 이하 인용된 횟수 카운팅
                c += 1

        if temp < k:    # k번 이상 인용된 논문이 k번 미만이라면
            pass
        # k번 이상 인용된 논문 k편 이상 & k번 이하 인용이 (n-k)편 이상 k 이하
        elif temp >= k and (n-k)<=c<=k:
            res = k
    return res

print(getQ(n))

'''
for k in range(1, n+1):
    temp = n - bisect_left(ref, k)
    c = bisect_right(ref, k)
'''