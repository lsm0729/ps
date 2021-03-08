import sys
import copy

def input_data():
    map_soli = [[0] + list(readl().strip()) + [0] if 1<=r<=5 else [0]*11 for r in range(7)]
    readl()
    return map_soli

readl = sys.stdin.readline
T = int(readl())




def dfs(cnt):
    global pin_num
    global count_ans
    global mm

    chk=False
    ## 옮길수 있는지 체크
    for y in range(1,6):
        for x in range(1,10):
            if mm[y][x]=='o':
                for dy, dx  in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny,nx = y+dy,x+dx
                    nny,nnx= ny+dy,nx+dx
                    ## 맵밖처리
                    if nny<1 or nny>5 or nnx<1 or nnx>9: continue
                    ## 옮길수 있는상황
                    if mm[ny][nx]=='o' and mm[nny][nnx]=='.':
                        chk= True
                        mm[y][x]='.'
                        mm[ny][nx]='.'
                        mm[nny][nnx]='o'
                        dfs(cnt+1)

                        mm[y][x]='o'
                        mm[ny][nx]='o'
                        mm[nny][nnx]='.'

    ## 못움직였으면 남은 말수를 체크
    if not chk:
        pin_candi = 0
        for y in range(1,6):
            for x in range(1,10):
                if mm[y][x]=='o':
                    pin_candi+=1
                    
                    
        if pin_candi<pin_num:
            pin_num=pin_candi
            count_ans=cnt
            return


for _ in range(T):
    # 입력받는 부분
    mm = input_data()
    # 여기서부터 작성

    pin_num=float('inf')
    count_ans = 0

    dfs(0)

    print(pin_num,count_ans)










