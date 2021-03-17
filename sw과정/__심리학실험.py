import sys

read = sys.stdin.readline


n = int(read())

order = list(map(int,read().split()))


ans = float('inf')

p1,p2 = -1,-1

l,r = 0,n-1

while l<r:

    tmp = order[l]+order[r]

    if abs(tmp)<ans:
        ans = abs(tmp)
        p1  = l
        p2  = r

    if tmp < 0 :
        l+=1

    else:
        r-=1

print(p1,p2)
