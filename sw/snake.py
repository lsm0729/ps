import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    K = int(readl())
    pos = [tuple(map(int, readl().split())) for _ in range(K)]
    L = int(readl())
    cmd_list = [list(readl().split()) for _ in range(L)]

    return N, K, pos, L, cmd_list



# 입력받는 부분
N, fruit_n, fruit_pos, move_n, move_list = input_data()

# 여기서부터 작성

# 출력하는 부분

#맵크기, 과일개수
#print(N,fruit_n)
# 맵 y,x = 하,우 1부터 시작


#과일위치 K개
#print(fruit_pos)
#뱀이동 회수
#print(move_n)
#뱀이동 커맨드
# L 이동방향기준 왼쪽으로, D 이동방향 기준 오른쪽으로.
#print(move_list)


def move(dir_idx):
    global time
    global current_snake_q
    global current_dir
    global mm


    dy, dx = dir_list[current_dir]

    duration,next_dir = move_list[dir_idx]
    duration= int(duration)
    #print(dy, dx,duration)
    while duration:
        time+=1
        duration-=1
        ## 확인만 하고 popup은 안함
        snake_head_y,snake_head_x = current_snake_q[0]
        next_snake_head_y,next_snake_head_x=snake_head_y+dy,snake_head_x+dx
        print(next_snake_head_y,next_snake_head_x)

        ## out of map return
        if next_snake_head_y<1 or next_snake_head_y>N or next_snake_head_x<1 or next_snake_head_x>N : return time


        ## next가 과일이면 뱀이랑은 마주칠이 없다는것이므로 처음 체크
        ## q 앞에 next값 넣고 continue
        if mm[next_snake_head_y][next_snake_head_x]==2:
            current_snake_q.appendleft((next_snake_head_y, next_snake_head_x))
            mm[next_snake_head_y][next_snake_head_x]=1
            continue

        ## 우선 머리를 이동해봄 1을 만나면 return
        if mm[next_snake_head_y][next_snake_head_x] == 1:
            return time



        ## 빈공간을 만난다면 next 위치 맵에 표기하고 q앞에 삽입.
        mm[next_snake_head_y][next_snake_head_x]=1
        current_snake_q.appendleft((next_snake_head_y, next_snake_head_x))
        snake_tail_y, snake_tail_x = current_snake_q.pop()
        mm[snake_tail_y][snake_tail_x]=0


    ## current_dir update
    #왼쪽으로  +1
    if next_dir == 'L':
        current_dir = (current_dir+1)%4
    # 오른쪽으로 -1
    else :
        current_dir = (current_dir-1)%4

    ## 계속진행에 대한 플래그
    return -1

dir_list=[(1,0),(0,1),(-1,0),(0,-1)]
## 하 우 상 좌
## L +1 D -1
mm=[[0]*(N+2) for _ in range(N+2)]
for y,x in fruit_pos:
    mm[y][x]=2
mm[1][1]=1
current_snake_q=deque()
current_snake_q.append((1, 1))
#print(mm)
#print(current_snake)

## 최초 값은 1 이다
current_dir=1
time = 0

for idx in range(move_n):
    candi=move(idx)
    if candi==-1 : continue

    print(candi)
    break






























