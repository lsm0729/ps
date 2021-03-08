import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int, readl().split())) for _ in range(N)]
    return N, pos


# 입력 받는 부분
N, pos = input_data()

#print(N)
#print(pos)


start_x,start_y = pos[0]


total=0
for x,y in pos[1:]:
    total+=abs(x-start_x)+abs(y-start_y)
    start_x,start_y=x,y

#print(total)

candi=0
for idx in range(1,N-1):

    pre_x,pre_y=pos[idx-1]
    cur_x,cur_y=pos[idx]
    nxt_x,nxt_y=pos[idx+1]

    do_not_skip = abs(cur_x-pre_x)+abs(cur_y-pre_y)+abs(nxt_x-cur_x)+abs(nxt_y-cur_y)
    skip        = abs(nxt_x-pre_x)+abs(nxt_y-pre_y)

    candi= max(candi,do_not_skip-skip)

print(total-candi)