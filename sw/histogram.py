import sys
from collections import deque
def input_data():
    readl = sys.stdin.readline
    N, *list_height = map(int,readl().split())
    return N, list_height



while 1:

    # 입력받는 부분
    N, list_height = input_data()
    if N == 0: break
    ans = 0
    stack = []
    for i in range(N):
        idx,height = i,list_height[i]
        print("current idx height")
        print(idx,height)
        if not stack:
            stack.append((idx,height))
            print(stack)
            continue

        while stack:

            top_idx,top_height = stack[-1]
            if top_height > height :
                ans = max(ans,top_height)
                print(top_idx,top_height)
                stack[-1]=(top_idx,height)
                print(stack)



            else:

                stack.append((id,height))
                print(stack)
                break











