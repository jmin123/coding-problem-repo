'''
Programmers 코딩테스트 연습
문제 이름 : 아이템 줍기
문제 설명 : 
지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.

만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.

즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.

다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.

한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

제한사항
rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
itemX, itemY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다. 
'''
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[0] * 102 for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 2
                else:
                    field[i][j] = 1

    print("Corrected output (problem coordinate system):")
    for y in range(20, 0, -1):  # y축을 20까지 표시 (2배 크기)
        for x in range(21):     # x축을 20까지 표시 (2배 크기)
            if field[x][y] == 1:
                print("■", end=' ')  # 경로를 ■로 표시
            elif field[x][y] == 2:
                print("□", end=' ')  # 내부를 □로 표시
            else:
                print(".", end=' ')  # 빈 공간을 .로 표시
        print(f" {y//2}")  # y축 좌표 표시 (원래 크기로 변환)
    for x in range(21):
        print(f"{x//2:2}", end='')  # x축 좌표 표시 (원래 크기로 변환)
    print()
    
    def bfs(startX, startY, targetX, targetY):
        queue = deque([(startX * 2, startY * 2, 0)])
        visited = [[0] * 102 for _ in range(102)]
        
        while queue:
            x, y, distance = queue.popleft()
            
            # 아이템의 위치에 도착하면 반환
            if x == targetX *2 and y == targetY * 2:
                return distance // 2
            
            for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                                
                # 범위 체크
                if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny] and field[nx][ny] == 1:
                    queue.append([nx,ny,distance+1])
                    visited[nx][ny] = 1
        
    return bfs(characterX, characterY, itemX, itemY)

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
