def max_path_sum(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]
    
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    return dp[0][0]