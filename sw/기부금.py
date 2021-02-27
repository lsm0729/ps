import sys

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    insentive = list(map(int, readl().split()))
    return N, M, insentive


N, M, insentive = input_data()

# N : 직원수
# M : 기부금 목표
# intensive : 직원별 성과급




def donate(std):
    tot = 0
    for x in insentive:
        if x>=std:
            tot+=(x-std)
    return tot


MAX = max(insentive)
MIN = min(insentive)

# start,end : 상한선  성과급 min max 값
# target    : 기부금 목표 M


def bs(start,end,target ):

    while start <= end :
        mid = (start+end)//2

        if target < donate(mid):
            end = mid-1

        else :
            start = mid+1

    return start


print(bs(MIN,MAX,M))



