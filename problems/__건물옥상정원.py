import sys
from collections import deque
readl = sys.stdin.readline


n = int(readl())
ll=[int(readl()) for _ in range(n)]+[1000000001]



stack = deque()
ans = 0


for idx, height in enumerate(ll):

    if (not stack) or stack[-1][1]>height:

        stack.append((idx,height))
        continue

    ## 현재 height가 stack 마지막 값보다 크거나 같다면
    if stack[-1][1]<=height:
        while stack:
            if stack[-1][1]>height:
                break
            c_idx,c_height = stack.pop()
            ans+=(idx-c_idx-1)


        stack.append((idx,height))

print(ans)









