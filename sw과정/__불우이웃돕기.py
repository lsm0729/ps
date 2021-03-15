import sys
read = sys.stdin.readline

n = int(read())
box  = list(map(int,read().split()))
ans  = [x for x in box]
base = [1,5,10,50,100,500,1000,3000,6000,12000]
"""
박스를 최대한 많이 보낸다 = 박스를 최소한으로 남긴다.
남는 물건 = 총 물건 - 보내야하는 물건

남는 물건을 만족하는 최소 박스의 개수를 구함.
"""

#print(box)
#print(ans)

total = 0

for x,y in zip(box,base):
    total+=x*y

total -=n

for i in reversed(range(10)):
    cnt    = total//base[i] if total/base[i]<=box[i] else box[i]
    total -= cnt*base[i]
    box[i]-=cnt
print(sum(box))
print(*box)
