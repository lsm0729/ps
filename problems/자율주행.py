# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_park = [list(readl()[:-1]) for _ in range(R)]
    return R, C, map_park


sol = -1

# 입력받는 부분
R, C, mm = input_data()

## y x

chk = [[False]*C for _ in range(R)]
# 여기서부터 입력


# 출력하는 부분
def bfs():
    q = deque()
    q.append((0,0,0))
    chk[0][0] =True

    while q:

        y,x,t = q.popleft()

        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ny, nx = y+dy, x+dx
            ## 맵밖처리
            if ny<0 or ny>=R or nx<0 or nx>=C : continue
            ## 도착 처리
            if ny==R-1 and nx==C-1:return t+1
            ## 공원 처리
            if mm[ny][nx]=='X': continue
            ## 기방문 처리
            if chk[ny][nx]==True : continue

            chk[ny][nx]=True
            q.append((ny,nx,t+1))

    return -1

print(bfs())





