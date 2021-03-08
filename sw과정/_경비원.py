import sys

def input_data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N+1)]
    return N, W, H, info

sol = -1

# 입력받는 부분
n,            W,               H,               info = input_data()
#상점개수      맵 가로           맵 세로
# 여기서부터 작성

# 출력하는 부분


#print(n)
#print(x,y)
#print(info)

shop=info[:n]
g_pos,g_len= info[-1]
#print(shop)
#print(g_pos,g_len)

ans = 0
parallel=[(1,2),(2,1),(3,4),(4,3)]
def get_coordinate(p,l):

    if p==1:
        return 0,l
    if p==2:
        return H,l
    if p==3:
        return l,0
    if p==4:
        return l,W

g_y,g_x =get_coordinate(g_pos,g_len)

#print(g_y,g_x)
#print(g_pos,g_len)
#print('-------------')
ans = 0
for pos,len in shop:
    tmp=0
    y,x = get_coordinate(pos,len)
    #print(y,x)
    #print(pos,len)
    ## 마주보는 면일경우
    if (pos,g_pos) in  parallel:

        ## 가로면끼리
        if g_pos<3:
            left=min(len,g_len)
            right=max(len,g_len)
            add =min(left,W-right)
            tmp=abs(y - g_y) + abs(x - g_x)+ 2*add




        ##세로면끼리
        else :
            upper=min(len,g_len)
            lower=max(len,g_len)
            add =min(upper,H-lower)
            tmp=abs(y - g_y) + abs(x - g_x)+ 2*add

    # 직각면일경우
    else :
        tmp= abs(y - g_y) + abs(x - g_x)
    ans+=tmp
    #print(tmp)


print(ans)

