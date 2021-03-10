"""
https://www.acmicpc.net/problem/9663


for-else 사용법 숙지..


for "xxxxxx":
    if "xxxx":
        break

else:
    for문이 break 하지않고 끝까지 돌면 else 문 실행.



"""


n = int(input())
def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count


print(dfs([0]*n,0,n))


