import sys
import itertools


def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    relation = [list(map(int, readl().split())) for i in range(M)]
    bonus = list(map(int, readl().split()))
    return N, M, relation, bonus


# 입력받는 부분
N, M, relation, bonus = input_data()

g=dict()

for u,d in relation:
    if u in g: g[u].append(d)
    else :
        g[u]=[d]


print(g)

bonus = sorted(bonus,reverse=True)

print(bonus)
bonus_chk =[False]*(N)
bonus_chk[0]=True

print('---------------------')
# 어느 사람이 얼마의 보너스를 받았나
bonus_list=[0]*(N+1)
bonus_list[1]=bonus[0]
count=1



def dfs(up):
    global count

    print(count)
    if count==N:
        print(bonus_list)
        return


    length= len(g[up])

    permu_list=[]















dfs(1)








