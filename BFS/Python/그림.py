from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                size += 1
    
    return size

count_paintings = 0
max_size_of_painting = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            max_size_of_painting = max(max_size_of_painting, bfs(i, j))
            count_paintings += 1
            
print(count_paintings)
print(max_size_of_painting)