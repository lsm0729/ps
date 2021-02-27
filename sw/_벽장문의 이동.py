import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    A, B = map(int, readl().split())
    S = int(readl())
    seq = [int(readl()) for _ in range(S)]
    return N, A, B, S, seq



#입력받는 부분
N,      A,   B,   S,      seq = input_data()
#문개수  열린문위치  순서개수  순서list

# 여기서부터 작성

def dfs(d1, d2, cnt, target_pos):
    global ans

    if target_pos==S:
        ans= min(ans,cnt)
        return

    dfs(seq[target_pos],d2,cnt+abs(d1-seq[target_pos]),target_pos+1)
    dfs(d1,seq[target_pos],cnt+abs(d2-seq[target_pos]),target_pos+1)



ans = float('inf')

dfs(A,B,0,0)
print(ans)


