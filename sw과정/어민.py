import sys
import copy


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


# 입력받는 부분
N, info = input_data()

# 여기서부터 작성

# 출력하는 부분


tmp = sorted(info, key=lambda x: x[1])

MIN = tmp[0][1]
MAX = tmp[-1][1]


def bs(start, end):
    while start <= end:
        mid = (start + end) // 2

        if is_available(mid):
            start = mid + 1

        else:
            end = mid - 1

    return end


def is_available(num):
    sum = 0

    for i in range(N-1):
        gap = info[i][1]-num
        sum+=gap
        if sum>=0 and sum-(info[i+1][0]-info[i][0])<0 :
            sum = 0

        else :
            sum-=info[i+1][0]-info[i][0]


    sum+=info[N-1][1]-num

    if sum>=0 :
        return True

    else :
        return False





    pass



print(bs(MIN, MAX))
