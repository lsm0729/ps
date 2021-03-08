import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    C, R = map(int, readl().split())
    map_zergling = [[0]+list(map(int, readl()[:-1]))+[0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    sc, sr = map(int, readl().split())
    return C, R, sc, sr, map_zergling


sol_time, sol_zergling = -1,-1

# 입력받는 부분
C, R, sc, sr, mm = input_data()

## 가로 세로 x y


chk = [[False]*(C+2) for _ in range(R+2)]


def bfs():
    q = deque()
    q.append((sr, sc, 3))

    chk[sr][sc] = True
    count = 1
    time = 3
    while q:
        y, x, t = q.popleft()
        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ny, nx = y + dy, x + dx

            ## 맵밖   처리
            if ny > R or ny < 1 or nx > C or nx < 1: continue
            ## 빈공간 처리
            if mm[ny][nx]==0: continue
            ## 기방문 처리
            if chk[ny][nx] == True: continue

            ## 새로운 저글링 이므로 count+=1
            count += 1
            ## 시간 갱신
            time = max(time, t + 1)

            chk[ny][nx] = True
            q.append((ny, nx, t + 1))

    return count, time


zz = 0
for y in range(R+2):
    for x in range(C+2):
        if mm[y][x]==1:
            zz+=1

count, time = bfs()

print(time)
print(zz-count)











