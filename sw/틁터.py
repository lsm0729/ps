import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_field = [list(map(int, readl().split())) for _ in range(N)]
    return N, map_field


sol = -1
# 입력받는 부분
N, mm = input_data()


print(mm)

for y in range(N):
    for x in range(N):
