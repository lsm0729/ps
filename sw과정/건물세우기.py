import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    cost = [list(map(int, readl().split())) for _ in range(N)]
    return N, cost

# 입력받는 부분
N, cost = input_data()



print(cost)


'''
4
11 12 18 40
14 15 13 22
11 17 19 23
17 14 20 28
'''


dp = [[float('inf'),0]for _ in range(2**N)]
dp[0]=[0,0]


## n번쨰 건물 0~n-1
def dfs(n,sum_cost,bit_mask):


    if bit_mask == 2**(N-1):
        print (dp[2**(N-1)][1])
        return


    ## n번쨰 건물에 대해 몇번쨰에 세울건지 ? i
    for idx in range(N):
        bm= bit_mask|2**idx
        nxt_cost =cost[n][idx]














