from collections import deque

from queue import PriorityQueue


import sys

def input_data():
    readl = sys.stdin.readline
    N, M = list(map(int, readl().split()))
    job = list(map(int, readl().split()))
    return N, M, job


T = int(sys.stdin.readline())
sol = []
chk = []
for _ in range(T):
    #입력받는 부분
    N, M, job = input_data()
    # 여기서부터 작성
    target= job[M]
    q  = deque()
    for idx in range(N):
        q.append ( (job[idx],idx) )



    count = 0
    while q :
        value,idx = q[0]


        if value == max(job) and value == target and idx == M:
            print(count+1)
            break
        else :

            if value == max(job):
                q.popleft()
                job.remove(value)
                count+=1

            else :
                q.rotate(-1)


























