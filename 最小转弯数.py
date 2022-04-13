
#假设给你一个01矩阵，和初始位置，终点位置，请问你怎么做到最少的拐弯次数到达终点，
#0代表可以经过，1代表有障碍物），不存在向后走
def minzhuanwan(matrix):
    if not matrix:
        return 0
    n=len(matrix)
    m=len(matrix[0])
    if n==1 or m==1:
        return 0
    dp=[[0 for i in range(m)] for j in range(n)]
    dp[0][0]=1
    for i in range(1,n):
        dp[i][0]=dp[i-1][0]+1
    for j in range(1,m):
        dp[0][j]=dp[0][j-1]+1
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]==0:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
            else:
                dp[i][j]=dp[i-1][j]+1
    return dp[n-1][m-1]