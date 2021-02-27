import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int, readl().split())) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, r_top, c_top, map_mountine


# 입력받는 부분
N, y_t, x_t, mm = input_data()

##

# 여기서부터 작성
INF = float('inf')
chk = [[INF] * (N + 2) for _ in range(N + 2)]


def bfs():
    q = deque()
    for x in range(1, N + 1):
        q.append((1, x, mm[1][x] ** 2))
        chk[1][x] = mm[1][x] ** 2

        q.append((N, x, mm[N][x] ** 2))
        chk[N][x] = mm[N][x] ** 2

    for y in range(2, N):
        q.append((y, 1, mm[y][1] ** 2))
        chk[y][1] = mm[y][1] ** 2

        q.append((y, N, mm[y][N] ** 2))
        chk[y][N] = mm[y][N] ** 2

    while q:
        y, x, v = q.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            ## 맵밖 처리
            if ny > N or ny < 1 or nx > N or nx < 1: continue

            ## ny nx 좌표 후보값구함
            if mm[ny][nx] > mm[y][x]:
                candi = v + ((mm[ny][nx] - mm[y][x]) ** 2)
            else:
                candi = v + abs(mm[ny][nx] - mm[y][x])
            ## 후보값이 현재 값보다 작으면 갱신하고 q에 삽입
            if candi < chk[ny][nx]:
                chk[ny][nx] = candi
                q.append((ny, nx, candi))

    return(chk[y_t][x_t])

print(bfs())
