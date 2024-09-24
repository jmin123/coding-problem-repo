import java.util.*;

class Solution {
    public int solution(String[] board) {
        int n = board.length;
        int m = board[0].length();
        int startX = 0, startY = 0;

        int dx[] = {1, 0, -1, 0};
        int dy[] = {0, 1, 0, -1};

        int boardInt[][] = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char c = board[i].charAt(j);
                if (c == 'R') {
                    boardInt[i][j] = 0;
                    startX = i;
                    startY = j;
                } else if (c == 'G') {
                    boardInt[i][j] = 1;
                } else if (c == 'D') {
                    boardInt[i][j] = -1;
                } else {
                    boardInt[i][j] = 0;
                }

                System.out.print(boardInt[i][j] + " ");
            }
            System.out.println();
        }

        Queue<int[]> queue = new LinkedList<>();
        // 시작 위치, 이동횟수
        queue.offer(new int[] {startX, startY, 0});
        boolean[][] visited = new boolean[n][m];
        visited[startX][startY] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int count = current[2];

            // 만약 목표지점에 도달하면 이동횟수 반환
            if (boardInt[x][y] == 1) {
                return count;
            }

            for (int i = 0; i < 4; i++) {
                // 계속해서 움직여야 하기 때문에 여기서 dx, dy를 더해주지 않는다.
                int nx = x;
                int ny = y;

                while (true) {
                    nx += dx[i];
                    ny += dy[i];

                    // 가로 막히거나 범위를 벗어나면 이전 위치로 rollback
                    if (nx < 0 || ny < 0 || nx >= n || ny >= m || boardInt[nx][ny] == -1) {
                        nx -= dx[i];
                        ny -= dy[i];
                        break;
                    }
                }
                
                // 멈춰선 위치를 방문처리하고 다시 큐에 넣어줘서 진행
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[] {nx, ny, count + 1});
                }
            }
        }

        return -1;
    }
}