import sys
from collections import deque


def input_data():
    L, R, C = map(int, readl().split())
    map_dungeon=[]
    for _ in range(L):
        tmp=[list(readl().strip()) for r in range(R)]
        map_dungeon.append(tmp)
        strip= input()



    return L, R, C, map_dungeon


readl = sys.stdin.readline

def bfs(c,b,a):
    global chk
    q=deque()
    q.append((c,b,a,0))
    chk[c][b][a]=True



    while q:

        z,y,x,t = q.popleft()

        for dz,dy,dx in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:


            nz,ny,nx= z+dz,y+dy,x+dx


            ## 맵밖처리
            if nz>=L or nz<0 or ny>=R or ny<0 or nx>=C or nx<0: continue

            ## 도착지 처리
            if mm[nz][ny][nx]=='E':
                print('Escaped in',t+1,'minute(s).')
                return
            ## 벽처리



            ## chk 처리
            if chk[nz][ny][nx]==True : continue
            #print(mm[nz][ny][nx])

            if mm[nz][ny][nx] == '#': continue

            chk[nz][ny][nx] = True

            q.append((nz,ny,nx,t+1))

    print('Trapped!')





while 1:
    # 입력 받는 부분
    L,    R,   C,  mm = input_data()
#   높이  세로  가로
    if L == 0 and R == 0 and C == 0: break
    s_z,s_y,s_x=0,0,0
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if mm[z][y][x]=='S':
                    s_z, s_y, s_x=z,y,x

    chk=[[[False]*C for _ in range(R)] for _ in range(L)]
    bfs(s_z, s_y, s_x)




