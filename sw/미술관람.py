import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_nor_pig







def bfs(b,a,color):
    global count
    q=deque()
    q.append((b,a))
    chk[b][a]=True

    while q :
        y,x =q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if ny<1 or ny>N or nx<1 or nx>N : continue
            if chk[ny][nx]: continue
            if mm[ny][nx]!=color : continue
            chk[ny][nx]=True
            q.append((ny,nx))
    count+=1

ans=[]
N, mm = input_data()
chk=[[False]*(N+2) for _ in range(N+2)]
count = 0

for y in range(1,N+1):
    for x in range(1,N+1):

        if chk[y][x]: continue
        bfs(y,x,mm[y][x])

ans.append(count)

chk=[[False]*(N+2) for _ in range(N+2)]
count=0

for y in range(1,N+1):
    for x in range(1,N+1):
        if mm[y][x]=='R': mm[y][x]='G'

for y in range(1,N+1):
    for x in range(1,N+1):

        if chk[y][x]: continue
        bfs(y,x,mm[y][x])

ans.append(count)

print(*ans)