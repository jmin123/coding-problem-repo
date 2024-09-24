from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0  # 섬의 개수를 저장할 변수
        rows = len(grid)  # 그리드의 행 수
        cols = len(grid[0])  # 그리드의 열 수

        def bfs(start_x, start_y, graph):
            dx = [1, 0, -1, 0]  # x축 방향 이동 배열
            dy = [0, 1, 0, -1]  # y축 방향 이동 배열

            queue = deque([(start_x, start_y)])  # BFS를 위한 큐 초기화
            grid[start_x][start_y] = '0'  # 방문한 노드를 '0'으로 표시하여 방문 처리

            while queue:
                x, y = queue.popleft()  # 큐에서 현재 노드를 꺼냄
                
                # 상, 하, 좌, 우 방향으로 이동하면서 인접한 노드를 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 범위를 벗어나지 않았고 아직 방문하지 않았다면
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'  # 방문 처리
                        queue.append((nx, ny))  # 큐에 추가하여 다음 탐색 대상으로 설정
                
        for i in range(rows):
            for j in range(cols):
                # 섬이 존재할 때만 BFS 시작
                if grid[i][j] == '1':
                    bfs(i, j, grid)  # BFS 호출
                    islands += 1  # 섬의 개수 증가

        return islands  # 최종 섬의 개수 반환