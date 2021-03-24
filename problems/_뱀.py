import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(input())
    K = int(input())
    pos = [tuple(map(int, input().split())) for _ in range(K)]
    L = int(input())
    cmd_list = [list(input().split()) for _ in range(L)]

    return N, K, pos, L, cmd_list



N, K, pos, L, cmd_list = input_data()



dir_list=[(1,0),(0,1),(-1,0),(0,-1)]
## 하 우 상 좌
## L +1 D -1
mm=[[0]*(N+2) for _ in range(N+2)]
for y,x in pos:
    mm[y][x]=2
mm[1][1]=1

## 최초 값은 1 이다
current_dir=1
time = 0


def move():
    global mm
    snake = deque()
    snake.append((1, 1))
    time=0
    # 초기값 : 0 우측이동
    current_dir=1
    dy, dx = dir_list[current_dir]

    dir_order = 0
    duration,next_dir = cmd_list[dir_order]
    duration= int(duration)

    while True:

        time+=1
        y,x = snake[0]
        ny,nx = y+dy, x+dx


        ## out of map
        if ny<1 or nx<1 or ny>N or nx>N:

            return time

        ## meet snake itself
        if mm[ny][nx]==1:

            return time

        ## meet fruit
        if mm[ny][nx]==2:
            snake.appendleft((ny,nx))
            mm[ny][nx]=1



        ## meet empty space
        if mm[ny][nx]==0:
            mm[ny][nx]=1
            snake.appendleft((ny,nx))
            tail_y, tail_x = snake.pop()
            mm[tail_y][tail_x]=0


        if time==duration :

            current_dir = (current_dir + 1) % 4 if next_dir == 'L' else (current_dir - 1) % 4
            dy,dx = dir_list[current_dir]

            dir_order+=1
            if dir_order==L: continue
            duration, next_dir = cmd_list[dir_order]
            duration = int(duration)



print(move())

