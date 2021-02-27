import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int, readl().split())) for _ in range(N)]
    return N, pos


# 입력받는 부분
n, pos = input_data()
N=100
# 여기서부터 작성


mm = [[-1] * (N+2) for _ in range(N+2)]
chk = [[False] * (N+2) for _ in range(N+2)]

for x,y in pos :
    mm[y][x] = 0
    chk[y][x]=True

def coloring(b,a):
    global sector
    global edge_sector
    q= deque()
    q.append((b,a))
    mm[b][a] = sector

    while q :
        y,x = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny,nx = y+dy,x+dx
            ## 맵밖처리
            if ny <1 or ny>N or nx<1 or nx>N:
                ##외부와 닿는 구역이면 추가
                edge_sector.add(sector)
                continue
            ## 체크 처리
            if chk[ny][nx]== True : continue
            q.append((ny,nx))
            chk[ny][nx]=True
            mm[ny][nx]=sector
    sector+=1


edge_sector=set()
sector = 1

for y in range(1,N+1):
    for x in range(1,N+1):
        if chk[y][x]== True : continue
        coloring(y,x)

## 건초가 직접 닿는 경우에 대해
edge_sector.add(-1)
round = 0
for x,y in pos :
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny,nx = y+dy,x+dx
        if mm[ny][nx] in edge_sector:
            round+=1

print(round)



