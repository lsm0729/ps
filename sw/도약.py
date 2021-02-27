import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos




# 입력받는 부분
N, pos = input_data()


def bs(s, e, target_value):
    while s <= e:
        mid = (s + e) // 2
        if pos[mid] < target_value:
            s = mid + 1
        else:
            e = mid - 1

    return s


pos = sorted(pos)
ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        jump1 = pos[j]-pos[i]
        ans+=bs(0,N-1,pos[j]+2*jump1+1)-bs(0,N-1,pos[j]+jump1)

print(ans)

################
#
#  bisect 모듈
#
#
#
#
#