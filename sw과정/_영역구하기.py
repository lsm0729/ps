"""
https://www.acmicpc.net/problem/2583
"""


import sys
from collections import deque

readl = sys.stdin.readline

r,c,k = map(int,readl().split())

pos = [list(map(int,readl().split())) for _ in range(k)]

##preprocess
chk= [[False]*c for _ in range(r)]
for bot_x,bot_y, top_x,top_y in pos:
    for y in range(bot_y,top_y):
        for x in range(bot_x,top_x):
            chk[y][x]=True
sector_no = 0
area      = []
#print(chk)
def bfs(y,x):
    global sector_no
    global area

    q = deque()
    q.append((y,x))
    chk[y][x]=True

    temp_area = 1
    while q:
        y,x= q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny,nx = y+dy,x+dx

            if ny<0 or nx<0 or ny>=r or nx>=c: continue
            if chk[ny][nx]: continue

            temp_area+=1
            chk[ny][nx]=True
            q.append((ny,nx))
    sector_no+=1
    area.append(temp_area)



for y in range(r):
    for x in range(c):
        if not chk[y][x]:
            bfs(y,x)


print(sector_no)
print(*sorted(area))







