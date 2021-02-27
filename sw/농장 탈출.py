import sys
import copy


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight


sol = -1
# 입력받는 부분
N, w = input_data()


'''
5
522
6
84
7311
19

'''




def summable(a, b):
    chk_len = min(len(str(a)), len(str(b)))
    check = True
    for _ in range(chk_len):
        ad = a % 10
        bd = b % 10
        if ad + bd >= 10:
            check = False
            break

        a = a // 10
        b = b // 10

    if check:
        return True
    else:
        return False

ans= 0

def dfs(n,sum_weight,cnt):
    global ans
    if n==N:
        ans=max(ans,cnt)
        return
    nxt_weight=w[n]

    if summable(sum_weight,nxt_weight):
        dfs(n+1,sum_weight+nxt_weight,cnt+1)
    dfs(n + 1, sum_weight , cnt)


dfs(0,0,0)
print(ans)



