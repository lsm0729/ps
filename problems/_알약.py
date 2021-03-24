"""
https://www.acmicpc.net/problem/4811

6
1
4
2
3
30
0


0이 들어오면 종료
한줄당 하나의 TC
"""
while True:
    n= int(input())

    if n==0: break

    mm =[[0]*(n+1) for _ in range(n+1)]

    mm[0]= [1]*(n+1)

    for y in range(1,n+1):
        #print(n-y)
        for x in range(n-y+1):
            if x==0:
                mm[y][x]=mm[y-1][x+1]
                continue
            mm[y][x]=mm[y-1][x+1]+mm[y][x-1]




    print(mm[-1][0])


