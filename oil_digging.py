from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_by_column = [0] * m
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
        
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        size = 0
        columns = set()
        
        while queue:
            i, j = queue.popleft()
            size += 1
            columns.add(j)
             
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                        
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and land[ni][nj] == 1:
                    visited[ni][nj] = True
                    queue.append((ni, nj))

        for col in columns:
            oil_by_column[col] += size
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j)
                
    return max(oil_by_column)