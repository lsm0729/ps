"""
https://www.acmicpc.net/problem/1309

4
"""

n,k = map(int,input().split())

def solve():
    mm = [[0]*(n+1) for _ in range(k+1)]

    """
    세로 k+1 (0-k)
    가로 n+1 (0-n)
    element 0 으로 초기화
    """


    mm[1]= [1]*(n+1)

    for y in range(2,k+1):
        mm[y][0]=1
        for x in range(1,n+1):
            mm[y][x]= mm[y-1][x]+mm[y][x-1]
    print(mm[-1][-1]%1000000000)

solve()
