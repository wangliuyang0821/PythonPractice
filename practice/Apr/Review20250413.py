import numpy as np


def uniquePaths(m: int, n: int) -> int:
    dp = np.zeros((m,n))
    for i in range(0,m):
        dp[i,0] = 1

    for i in range(0,n):
        dp[0,i] = 1

    for x in range(1,m):
        for y in range(1,n):
            dp[x,y] = dp[x - 1,y] + dp[x,y-1]
    return dp[m-1,n-1]

print(uniquePaths(3,7))