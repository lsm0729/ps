import sys

def input_data():
    readl = sys.stdin.readline

    door_num       = int(readl())
    open_1, open_2 = map(int,readl().split())
    seq_len        = int(readl())
    seq            = [int(readl()) for _ in range(seq_len)]

    return door_num,open_1,open_2,seq_len,seq


N,A,B,S,seq = input_data()

ans = float('inf')

##TODO: d1:열린문1, d2:열린문2,
## count:seq 진행하면서 누적된 이동횟수, seq_pos: seq의 pos

def dfs(d1,d2,count,seq_pos):
    global ans

    ##TODO: seq 마지막까지 순회하면 ans를 갱신한다.
    ##TODO: 최종적으로는 DFS 다돌고 최종 min 값이 반환됨.
    if seq_pos ==S:
        ans = min(ans,count)
        return

    ##TODO: d1을 움직여 빈문을 만들거나 d2를 움직여 d2를 만들거나 계속 선택해서 DFS 진행함

    ## d2 이동
    dfs(d1,seq[seq_pos],count+abs(d2-seq[seq_pos]),seq_pos+1)
    ## d1 이동
    dfs(seq[seq_pos],d2,count+abs(d1-seq[seq_pos]),seq_pos+1)


dfs(A,B,0,0)

print(ans)



