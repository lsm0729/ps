import sys
from collections import deque
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height


sol_list = []
# 입력받는 부분
N, height = input_data()
stack = deque()
ans = [0]*N
# 여기서부터 작성

# 출력하는 부분
for i in range(N):
    idx = i
    if not stack:
        stack.append((height[i],idx))
        continue

    while stack and stack[-1][0]< height[i]:
        ans[stack[-1][1]]=i+1
        stack.pop()
    stack.append((height[i],idx))






for x in ans:
    print(x)

