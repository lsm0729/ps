"""
https://www.acmicpc.net/problem/9207

첫째 줄에 테스트 케이스의 개수 1 ≤ N ≤ 100이 주어진다.
각 테스트 케이스는 게임판의 초기 상태이다.

게임판은 모두 같은 모양을 가진다.
(예제 참고) '.'는 빈 칸, 'o'는 핀이 꽂혀있는 칸,
'#'는 구멍이 없는 칸이다. 핀의 개수는 최대 8이며,
각 테스트 케이스는 빈 줄로 구분되어져 있다.

3
###...###
..oo.....
.....oo..
.........
###...###

###...###
..oo.o...
...o.oo..
...oo....
###...###

###o..###
.o.oo....
o.o......
.o.o.....
###...###

"""

import sys
readl = sys.stdin.readline

def input_data():
    mm = [list(readl()[:-1]) for _ in range(5)]
    readl()
    return mm



def solve(cnt):
    global count_ans
    global pin_ans
    global mm
    """
    세로 5
    가로 9
    고정
    """
    moved = False
    for y in range(5):
        for x in range(9):
            if mm[y][x]=='o':
                for dy , dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ny,nx   = y+dy,  x+dx
                    nny,nnx = ny+dy, nx+dx
                    ## 맵밖 처리
                    if nny<0 or nnx<0 or nny>4 or nnx>8: continue
                    ## 옮길수 있는 상황
                    if mm[ny][nx]=='o' and mm[nny][nnx]=='.':
                        ## Back Tracking 수행
                        moved=True
                        mm[y][x]     = '.'
                        mm[ny][nx]   = '.'
                        mm[nny][nnx] = 'o'

                        solve(cnt+1)

                        mm[y][x]='o'
                        mm[ny][nx]='o'
                        mm[nny][nnx]='.'

    ##맵을 다돈후 움직인 핀이 없다면 기존 값과 비교 진행
    if not moved:
        pin_left = 0
        for line in mm:
            for m in line:
                if m=='o': pin_left+=1

        if pin_left<pin_ans:
            pin_ans = pin_left
            count_ans=cnt
            return


tc = int(readl())

for _ in range(tc):

    mm=input_data()
    count_ans = 0
    pin_ans   = float('inf')

    solve(0)

    print(pin_ans,count_ans)




