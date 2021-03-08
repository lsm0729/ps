import sys
readl = sys.stdin.readline
"""
https://www.acmicpc.net/problem/6549
"""
while True:

    N, *l=list(map(int, readl().split()))
    if N == 0: break
    l.append(0)
    print(l)
    s=[]
    a=0
    for i,h in enumerate(l):
        print("================")
        print("current index : {}  height : {}".format(i,h))
        ## 이번 높이가 마지막꺼보다 작아지면 체크 진행
        print(s)
        while s and l[s[-1]]>h:

            print("s is not empty and top is lower then current height ")
            ## ih = 직전 블럭의 놓이

            ih=l[s.pop()]
            print("top height : {}".format(ih))
            print("stack after pop : {}".format(s))

            # i에서부터 s의 top까지의 거리를 가로길이로 한다.
            # w = i일때는 마지막일 때
            w=i-s[-1]-1 if s else i
            print("width : {}".format(w))
            print("candi area : {}".format(w*ih))
            if a<w*ih:
                print("candi is larger then ans, update ans")
                a=w*ih

        ## (스텍이 비거나) 높이가 단조증가하면 계속 집어넣음
        print("stack is empty or height is bigger or same")
        s.append(i)
    print(a)
