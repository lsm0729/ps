from sys import stdin
read = stdin.readline
T= int(read())

dp = [[0 for j in range(1001)] for i in range(1001)]




for _ in range(T):
    n,a,b = map(int,read().split())

MOD = 1000000007

for i in range(1,1001):
    for j in range(1001):
        if i == 1 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD
            if j - i - 1 >= 0:
                dp[i][j] += (MOD - dp[i-1][j-i-1]);
                dp[i][j] %= MOD