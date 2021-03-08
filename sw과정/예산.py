import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M




# 입력받는 부분
N, needs, M = input_data()


def budget(target):
    v = 0
    for candi in needs:
        if candi <=target:
            v+=candi
        else :
            v+=target
    return v



def bs(start,end,value):

    while start<=end :
        mid = (start+end)//2

        if value<budget(mid):
            end= mid-1

        else :
            start =mid+1

    return start




total = sum(needs)

if total<=M:
    print( max(needs))




else :
    MAX= max(needs)
    MIN= min(needs)

    ans = bs(MIN,MAX,M)
    if budget(ans)>M:
        ans-=1
    print(ans)