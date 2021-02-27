import sys


def input_data():
    readl = sys.stdin.readline
    return [list(map(int, readl().split())) for _ in range(9)]


# 입력받는 부분
mm = input_data()

'''

0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

'''


# x축 고정
def chk_row(x, n):
    for y in range(9):
        if mm[y][x] == n: return False
    return True


# y축 고정정
def chk_col(y, n):
    for x in range(9):
        if mm[y][x] == n: return False
    return True


# 박스설정
def chk_box(y, x, n):
    y = y // 3
    x = x // 3
    for r in range(3 * y, 3 * (1 + y)):
        for c in range(3 * x, 3 * (1 + x)):
            if mm[r][c] == n:
                return False
    return True

'''
def chk_all(y, x, n):
    if chk_row(x, n) and chk_col(y, n) and chk_box(y, x, n): return True
    return False
'''

def dfs(zeros_idx, cnt):
    global mm
    global breakcode

    # print('cnt ',cnt)
    if cnt == zero_num:
        breakcode=True

        for line in mm:
            print(*line)
        return

    y, x = zeros[zeros_idx]

    for num in range(1, 10):

        if not chk_row(x,num) : continue
        if not chk_col(y,num): continue
        if not chk_box(y,x,num) : continue
        mm[y][x] = num
        dfs(zeros_idx + 1, cnt + 1)
        if breakcode : return
        mm[y][x] = 0
    return


zeros = []

for y in range(9):
    for x in range(9):
        if mm[y][x] == 0:
            zeros.append([y, x])

zero_num = len(zeros)
# print(zeros)
# print(zero_num)
breakcode = False

dfs(0, 0)
