# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def input_data():
    N = int(input())
    sc, sr = map(int, input().split())
    map_city = [list(map(int,input(),[16]*(N))) for r in range(N)]
    return N, sc, sr, map_city



# 입력받는 부분
N, x, y, mm = input_data()

# 여기서부터 작성

# 출력하는 부분
print(N)
print(y,x)

print(mm)

dir_idx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# 위 아래 오른쪾 왼쪽

pipe=[(),(2,3),(0,1),(1,2),
      (1,3),(0,3),(0,2),(0,1,2),
      (1,2,3),(0,1,3),(0,2,3),(0,1,2,3)]
chk = [[False]*N for _ in range(N)]

def


