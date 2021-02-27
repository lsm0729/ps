import sys
from collections import deque
def input_data():
    readl = sys.stdin.readline
    n = int(readl())
    mm = [list(map(int, readl()[:-1])) for _ in range(n)]
    return n,mm

n,mm = input_data()

def bfs():
    INF = float('inf')
    chk = [[INF]*n for _ in range(n)]
    q= deque()

    q.append((0,0,0))
    # y,x, cost
    chk[0][0]=0
    while q:
        y,x,cost = q.popleft()

        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny,nx = y+dy, x+dx


            ## out of bound check
            if ny>=n or nx>=n or ny<0 or nx<0 : continue

            ## 계산된 cost가 현재 chk의 값보다 크면 continue
            temp_cost = cost+mm[ny][nx]
            if temp_cost >= chk[ny][nx]: continue

            chk[ny][nx] = temp_cost
            q.append((ny,nx,temp_cost))
    return chk[-1][-1]

print(bfs())