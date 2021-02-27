import sys
from collections import deque
import string
import copy


def input_data():
    readl = sys.stdin.readline
    P = int(readl())
    infos = [(lambda x: [x[0], x[1], int(x[2])])(readl().split()) for _ in range(P)]
    return P, infos


# 입력받는 부분
P, infos = input_data()

# 여기서부터 작성


# 출력하는 부분

##print(P)
##print(infos)


INF = float('inf')

## y 출발 x 도착
## abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
## 0~25 26~50,51
alpha = string.ascii_letters
mm = [[INF] * 52 for _ in range(52)]
startpoint=set()
q= deque()
for f, t, d in infos:
    if f == t : continue
    f_idx = alpha.index(f)
    t_idx = alpha.index(t)
    print(f,f_idx,t,t_idx)
    if f_idx>=26 and f_idx<=50:
        startpoint.add(f+t)

    if t_idx>=26 and t_idx <= 50:
        startpoint.add(t+f)
    mm[f_idx][t_idx] = min(mm[f_idx][t_idx], d)
    mm[t_idx][f_idx] = min(mm[t_idx][f_idx], d)
chk={}
for s in alpha:
    chk[s]=INF
for path in startpoint:
    s,e=path[0],path[1]
    q.append (([path],mm[alpha.index(s)][alpha.index(e)]))
    chk[s]=min(chk[s],mm[alpha.index(s)][alpha.index(e)])
    chk[e]=min(chk[e],mm[alpha.index(s)][alpha.index(e)])

print(q)
print(chk)

del startpoint






def bfs():



    while q :

        path,distance = q.popleft()

        end = path[-1][1]
        num_end = alpha.index(end)

        for i in mm[num_end]:
            if i== num_end : continue
            if distance+mm[num_end][i] >=chk[end]: continue
            nextpath = copy.deepcopy(path)
            nextpath.append(
                
            )



















'''
def bfs():
    startpoint = ''
    startpoint_check = float('inf')
    while q:

        ## 현재까지 path , 거기까지 오는데 걸린시간
        path, d = q.popleft()

        # path 마지막 지점에 대해 연겨되어있는 포인트에 대한 정보
        for candi, dist in graph[path[-1]]:
            ## 후보 포인트가 path에 있다면 continue
            if candi in path: continue

            ## 후보 path 로 갔을떄의 시간이 현재 시간 보다 크다면 continue
            if d + dist >= chk[candi]: continue

            chk[candi] = d + dist
            path.append(candi)
            q.append([path, d + dist])
            if candi == 'Z':
                if d + dist < startpoint_check:
                    startpoint = path[0]

    return startpoint, chk['Z']

'''