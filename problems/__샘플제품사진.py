import sys
from collections import deque
read = sys.stdin.readline

n = int(read())

q     = deque()
ID    = set()
order = []
check = dict()
for _ in range(n):
    pos,id = map(int,read().split())
    ID.add(id)
    order.append((id,pos))



order.sort(key=lambda x : x[1])
#print(order)
#print(ID)
ans = float('inf')
cnt = 0
for id,pos in order:
    #print("==============")
    #print(cnt)
    cnt+=1
    #print(id,pos)

    if id in ID:

        q.append([id,pos])
        try:
            check[id]+=1
        except:
            check[id]=1
        ID.remove(id)
        #print(check)
        if not ID:
            while True:
                id,pos = q[0]

                if check[id]==1:
                    break
                q.popleft()
                check[id]-=1
            ans = min((q[-1][1]-q[0][1]),ans)
            id,pos = q.popleft()
            ID.add(id)
        #print(q)
        continue

    if id not in ID:
        if q[-1][0]==id:
            check[id]-=1
            q.pop()
        while q:
            if q[0][0]==id:
                q.popleft()
                check[id]-=1
                continue
            break
        q.append([id,pos])
        check[id]+=1
        #print(q)
        continue

#print("++++++++++++++++++++++++++++")
print(ans)




