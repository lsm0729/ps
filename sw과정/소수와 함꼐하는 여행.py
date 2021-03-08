import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    S, E = map(int, readl().split())
    return S, E



# 입력받는 부분
S,E = input_data()


## 소수면 1 아니면 0
def is_prime(n):
    for i in range(2,n):
        if n%i==0:

            return 0

    return 1


def is_prime2(n):
    pass




## 한자리수 차이나면 1 아니면 0
def digit(a,b):
    a = str(a)
    b = str(b)
    count = 0
    for i in range(4):
        if a[i]!=b[i]:
            count+=1
            if count>=2 : return 0
    return 1


prime=[]

for x in range(1000,10000):
    if is_prime(x)==1:
        prime.append(x)


chk   = [False]*10000


def bfs():
    q = deque()

    q.append((S,0))

    chk[S]=True

    while q:
        n,d= q.popleft()

        for x in prime:

            ## 방문처리
            if chk[x]==True : continue
            ## 자리수 차이
            if digit(x,n)==0 : continue
            ## 소수처리
            if is_prime(x)==0: continue
            ## 종료처리
            if x == E: return d+1
            chk[x]=True
            q.append((x,d+1))

    return -1


print(bfs())


