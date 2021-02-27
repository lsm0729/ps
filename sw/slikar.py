import sys
from collections import deque


def input_data():
    R, C = map(int, readl().split())
    map_forest = [list(readl()[:-1]) for _ in range(R)]
    return R, C, map_forest


# 입력받는 부분
readl = sys.stdin.readline
T = int(readl())


def bfs():
    global MM
    q = deque()
    ## 물이 먼저 처리 되도록 앞에 넣음
    for w in water:
        q.append(w)
    q.append((sy, sx, 0))
    chk[sy][sx] = True

    while q:
        y, x, v = q.popleft()
        ## 물 처리
        if v == -1:
            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ny, nx = y + dy, x + dx
                ## 맵밖 처리
                if ny >= R or ny < 0 or nx >= C or nx < 0: continue
                ## 돌 처리
                if MM[ny][nx] == 'X': continue
                ## 도착지 처리
                if MM[ny][nx] == 'D': continue
                ## chk 유무 처리
                if water_check[ny][nx] == True: continue

                water_check[ny][nx] = True
                MM[ny][nx] = -1
                q.append((ny, nx, -1))
        ##이동시간 처리
        else:
            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ny, nx = y + dy, x + dx

                ## 맵밖 처리
                if ny >= R or ny < 0 or nx >= C or nx < 0: continue
                ## 도착지 처리
                if MM[ny][nx] == 'D': return (v + 1)
                ## 돌 처리
                if MM[ny][nx] == 'X': continue
                ## 물   처리
                if MM[ny][nx] == -1: continue
                ## 체크 처리
                if chk[ny][nx] == True: continue

                chk[ny][nx] = True
                q.append((ny, nx, v + 1))

    return 'KAKTUS'


for _ in range(T):
    R, C, MM = input_data()
    chk = [[False] * C for _ in range(R)]
    water_check = [[False] * C for _ in range(R)]
    water = []

    for y in range(R):
        for x in range(C):

            point = MM[y][x]

            if point == 'S':
                sy, sx = y, x
            elif point == '*':
                MM[y][x] = -1
                water.append((y, x, -1))
                water_check[y][x] = True
            ## D , 바위에 대해서는 continue
            else:
                continue

    print(bfs())
