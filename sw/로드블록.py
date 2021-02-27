import sys
from collections import deque
import copy
def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [map(int, readl().split()) for _ in range(M)]
    return N, M, edges


# 입력받는 부분
N, M, edges = input_data()

# 필드개수, 패스 개수, 패스
INF=float('inf')
chk= [INF]*(N+1)
graph={}
for s,e,d in edges :

    if s not in graph:
        graph[s]=[(e,d)]


    else :
        graph[s].append((e,d))

    if e not in graph:
        graph[e]=[(s,d)]
    else :
        graph[e].append((s,d))


q=deque()

for e,d in graph[1]:
    q.append(   [ [[1,e]],d ]   )
    chk[e]=d
chk[1]=0

print(chk)
chk1={}
for i in range(1,N+1):
    chk1[i]=

def bfs():
    v=INF
    p=list()
    while q :
        path,distance = q.popleft()

        end = path[-1][1]

        for e,d in graph[end]:
            if distance+ d >= chk[e]: continue
            nextpath=copy.deepcopy(path)
            nextpath.append([end,e])
            chk[e]=distance+d
            q.append([nextpath,distance+d])
            if e == N:
                if distance+d<v:
                    v=distance+d
                    p=nextpath

    return v,p



def bfs_re():
    v=INF
    p=list()
    while q :
        path,distance = q.popleft()

        end = path[-1][1]

        for e,d in graph[end]:
            if distance+ d >= chk[e]: continue
            nextpath=copy.deepcopy(path)
            nextpath.append([end,e])
            chk[e]=distance+d
            q.append([nextpath,distance+d])
            if e == N:
                if distance+d<v:
                    v=distance+d
                    p=nextpath

    return v,p






ans,path_candi= bfs()

print(path_candi)
print(graph)


for cs,ce in path_candi :


    pass