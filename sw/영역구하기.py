import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C, K = map(int, readl().split())
    rects = [list(map(int,readl().split())) for _ in range(K)]
    return R, C, K, rects


# 입력받는 부분
y_, x_, n, pos = input_data()





chk = [[False]*(x_+2) for _ in range(y_+2)]

for bot_x,bot_y,top_x,top_y in pos :
    bot_y+=1
    bot_x+=1

    for y in range(bot_y,top_y+1):
        for x in range(bot_x,top_x+1):
            chk[y][x]=True


sector=0
area=[]
def bfs(b,a):
    global sector
    global area
    area_size=1
    q= deque()
    q.append((b,a))
    chk[b][a]=True
    while q:
        y,x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if ny<1 or ny>y_ or nx<1 or nx>x_ : continue
            if chk[ny][nx]: continue
            chk[ny][nx]=True
            q.append((ny,nx))
            area_size+=1

    area.append(area_size)
    sector+=1


for y in range(1,y_+1):
    for x in range(1,x_+1):
        if chk[y][x]: continue
        bfs(y,x)
print(sector)
print(*sorted(area))

