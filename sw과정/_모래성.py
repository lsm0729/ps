import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_sand = [list(readl()[:-1])for _ in range(R)]
    return R, C, map_sand


## preprocess
r, c, mm = input_data()
sand= deque()
count= 0
for y in range(r):
    for x in range(c):
        if mm[y][x]=='.':
            mm[y][x]=0
            sand.append((y,x))
            #chk[y][x]=True
        else :
            mm[y][x]=int(mm[y][x])

## main function
def bfs():
    global mm
    global sand
    global count

    while True:

        ll = len(sand)
        ## 각각의시도떄 마다 큐에 들어있는 빈모래 주변의 모래성을 1씩 깍아 0 이되면 큐에 넣는다. 큐 한번 돌때마다 파도 한번 친것
        ## 추가된 빈모래에 대해서만 주변 모래성 깍아내면 됨. 기존에 빈모래의 영향은 이미 맵에 반영됨
        ## 한번 돌았는데 큐가 비었다는 것은 기존 트라이떄와 모래성 분포가 같다는 것이므로 결과 반환. 종료
        for _ in range(ll):
            y, x = sand.popleft()
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                ny, nx = y + dy, x + dx
                if ny >= r or ny < 0 or nx >= c or nx < 0: continue
                if mm[ny][nx] == 0: continue

                mm[ny][nx] -= 1

                if mm[ny][nx] == 0:
                    sand.append((ny, nx))

        if not sand: return
        count += 1




bfs()

print(count)