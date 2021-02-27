import sys


def input_data():
    N, B = map(int, readl().split())
    height = [int(readl()) for _ in range(N)]
    return N, B, height


readl = sys.stdin.readline
T = int(readl())


def dfs(n, sum_height):
    global ans

    if sum_height>=B :

        ans = min(ans, sum_height)
        return
    if n==N:
        return


    nxt_weight = h[n]
    dfs(n + 1, sum_height + nxt_weight)
    dfs(n + 1, sum_height)



for _ in range(T):
    # 입력받는 부분
    N, B, h = input_data()

    ans = float('inf')
    dfs(0,0)
    print(ans-B)