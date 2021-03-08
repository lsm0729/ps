import sys


def input_data():
    n = map(int, readl().split())
    result = [[next(n) for w in range(3)] for t in range(6)]
    return result

readl = sys.stdin.readline


def dfs(game):
    global candi

    # 모든 경기 다 수행 했을때 체크
    if game == 15:
        chk = True
        for i in range(6):
            for j in range(3):
                if candi[i][j]!=result[i][j]:
                    chk = False
                    break

        return chk


    #승패 무무 패승 케이스
    for i in range(3):

        if result[match[game][0]][i] == 0 or result[match[game][1]][2 - i] == 0:continue

        candi[match[game][0]][i] -= 1
        candi[match[game][1]][2 - i] -= 1


        if dfs(game + 1): return True

        candi[match[game][0]][i] += 1
        candi[match[game][1]][2 - i] += 1


    return False


ans = []
match = []

# 경기 순서
for i in range(5):
    for j in range(i + 1, 6):
        match.append((i, j))

for _ in range(4):
    result = input_data()
    candi = [[0, 0, 0] for _ in range(6)]

    if dfs(0):
        ans.append(1)
    else:
        ans.append(0)

print(*ans)