from collections import deque
from typing import List, Tuple

def extract_shapes(grid: List[List[int]], target: int) -> List[List[Tuple[int, int]]]:
    """
    주어진 그리드에서 특정 값(target)을 가진 모든 연결된 모양을 추출하여 반환합니다.

    Parameters:
    - grid (List[List[int]]): 입력 그리드 (game_board 또는 table).
    - target (int): 추출할 셀의 값 (game_board는 0, table은 1).

    Returns:
    - List[List[Tuple[int, int]]]: 모든 모양의 리스트. 각 모양은 (x, y) 튜플의 리스트로 표현됩니다.
    """
    n = len(grid)  # 그리드의 크기
    visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 여부를 저장하는 2D 리스트
    shapes = []  # 발견된 모든 모양을 저장할 리스트

    # 상, 하, 좌, 우 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 그리드의 모든 셀을 순회
    for i in range(n):
        for j in range(n):
            # 현재 셀이 타겟값을 가지고 있고, 아직 방문하지 않았다면
            if grid[i][j] == target and not visited[i][j]:
                shape = []  # 현재 모양의 좌표들을 저장할 리스트
                queue = deque()  # BFS를 위한 큐 초기화
                queue.append((i, j))  # 시작점 큐에 추가
                visited[i][j] = True  # 방문 표시

                # BFS 시작
                while queue:
                    x, y = queue.popleft()  # 큐에서 좌표를 하나 꺼냄
                    shape.append((x, y))   # 현재 좌표를 모양에 추가

                    # 상, 하, 좌, 우 인접 셀을 탐색
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        # 인접 셀의 좌표가 그리드 범위 내에 있는지 확인
                        if 0 <= nx < n and 0 <= ny < n:
                            # 인접 셀이 타겟값을 가지고 있고, 아직 방문하지 않았다면
                            if grid[nx][ny] == target and not visited[nx][ny]:
                                queue.append((nx, ny))  # 큐에 추가
                                visited[nx][ny] = True   # 방문 표시

                # 모양 정규화
                # 모든 좌표에서 최소 x와 최소 y를 찾아서, 좌표를 이동시킴
                min_x = shape[0][0]
                min_y = shape[0][1]
                
                for coord in shape:
                    if coord[0] < min_x:
                        min_x = coord[0]
                    if coord[1] < min_y:
                        min_y = coord[1]

                normalized_shape = []  # 정규화된 모양의 좌표들을 저장할 리스트
                for coord in shape:
                    normalized_x = coord[0] - min_x
                    normalized_y = coord[1] - min_y
                    normalized_shape.append((normalized_x, normalized_y))

                # 좌표들을 정렬하여 일관된 순서를 유지
                normalized_shape_sorted = sorted(normalized_shape)

                # 발견된 모양을 shapes 리스트에 추가
                shapes.append(normalized_shape_sorted)

    return shapes

def rotate(shape: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    주어진 모양을 90도 시계 방향으로 회전시킵니다.

    Parameters:
    - shape (List[Tuple[int, int]]): 회전시킬 모양의 좌표 리스트.

    Returns:
    - List[Tuple[int, int]]: 회전된 모양의 좌표 리스트.
    """
    rotated_shape = []  # 회전된 좌표들을 저장할 리스트

    # 각 좌표를 90도 시계 방향으로 회전
    for coord in shape:
        x = coord[0]
        y = coord[1]
        rotated_shape.append((y, -x))

    # 회전된 좌표들을 정렬하여 일관된 순서를 유지
    rotated_shape_sorted = sorted(rotated_shape)

    return rotated_shape_sorted

def get_all_rotations(shape: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    """
    주어진 모양의 모든 독특한 회전 형태를 생성하여 반환합니다.

    Parameters:
    - shape (List[Tuple[int, int]]): 원본 모양의 좌표 리스트.

    Returns:
    - List[List[Tuple[int, int]]]: 모든 독특한 회전된 모양의 리스트.
    """
    rotations = []  # 모든 회전된 모양을 저장할 리스트
    current_shape = shape  # 현재 회전할 모양을 저장

    for rotation_count in range(4):
        # 현재 모양을 회전
        rotated = rotate(current_shape)

        # 회전된 모양을 정규화
        # 최소 x와 y를 찾아서 모든 좌표를 이동
        min_x = rotated[0][0]
        min_y = rotated[0][1]
        for coord in rotated:
            if coord[0] < min_x:
                min_x = coord[0]
            if coord[1] < min_y:
                min_y = coord[1]

        normalized_rotated_shape = []  # 정규화된 회전된 모양의 좌표를 저장할 리스트
        for coord in rotated:
            normalized_x = coord[0] - min_x
            normalized_y = coord[1] - min_y
            normalized_rotated_shape.append((normalized_x, normalized_y))
        
        # 좌표들을 정렬하여 일관된 순서를 유지
        normalized_rotated_shape_sorted = sorted(normalized_rotated_shape)

        # 이미 존재하지 않는 형태라면 추가
        already_exists = False
        for existing_shape in rotations:
            if existing_shape == normalized_rotated_shape_sorted:
                already_exists = True
                break

        if not already_exists:
            rotations.append(normalized_rotated_shape_sorted)

        # 다음 회전을 위해 현재 모양 업데이트
        current_shape = normalized_rotated_shape_sorted

    return rotations

def solution(game_board: List[List[int]], table: List[List[int]]) -> int:
    """
    게임 보드의 빈 공간에 테이블의 퍼즐 조각을 규칙에 맞게 채워넣은 후,
    채워진 셀의 총 개수를 반환합니다.

    Parameters:
    - game_board (List[List[int]]): 게임 보드의 현재 상태.
    - table (List[List[int]]): 테이블 위의 퍼즐 조각들.

    Returns:
    - int: 채워진 셀의 총 개수.
    """
    # Step 1: 게임 보드에서 모든 빈 공간 추출 (target=0)
    empty_spaces = extract_shapes(game_board, 0)

    # Step 2: 테이블에서 모든 퍼즐 조각 추출 (target=1)
    puzzle_pieces = extract_shapes(table, 1)

    # Step 3: 각 퍼즐 조각에 대해 모든 회전 형태 생성
    rotated_pieces = []  # 모든 퍼즐 조각의 회전된 형태를 저장할 리스트
    for piece in puzzle_pieces:
        rotations = get_all_rotations(piece)
        rotated_pieces.append(rotations)

    used = [False for _ in rotated_pieces]  # 각 퍼즐 조각의 사용 여부를 저장하는 리스트
    answer = 0  # 채워진 셀의 총 개수를 저장할 변수

    # Step 4: 빈 공간과 퍼즐 조각을 매칭
    for space in empty_spaces:
        # 현재 빈 공간과 일치하는 퍼즐 조각을 찾기 위해 모든 퍼즐을 순회
        for idx, piece_rotations in enumerate(rotated_pieces):
            if used[idx]:
                continue  # 이미 사용된 퍼즐 조각은 건너뜀

            # 퍼즐 조각의 모든 회전 형태를 확인
            for rotated_piece in piece_rotations:
                if space == rotated_piece:
                    # 일치하는 퍼즐 조각을 찾았으므로, 채우기
                    answer += len(space)  # 채워진 셀의 개수를 더함
                    used[idx] = True      # 퍼즐 조각을 사용된 것으로 표시
                    break  # 현재 빈 공간에 퍼즐 조각을 채웠으므로 다음 빈 공간으로 이동

            if used[idx]:
                break  # 퍼즐 조각을 채웠으므로 다음 빈 공간으로 이동

    return answer

def main():
    # Test Case 1
    game_board1 = [
        [1,1,0,0,1,0],
        [0,0,1,0,1,0],
        [0,1,1,0,0,1],
        [1,1,0,1,1,1],
        [1,0,0,0,1,0],
        [0,1,1,1,0,0]
    ]

    table1 = [
        [1,0,0,1,1,0],
        [1,0,1,0,1,0],
        [0,1,1,0,1,1],
        [0,0,1,0,0,0],
        [1,1,0,1,1,0],
        [0,1,0,0,0,0]
    ]

    result1 = solution(game_board1, table1)
    print(f"Test Case 1 Result: {result1} (Expected: 14)")

    # Test Case 2
    game_board2 = [
        [0,0,0],
        [1,1,0],
        [1,1,1]
    ]

    table2 = [
        [1,1,1],
        [1,0,0],
        [0,0,0]
    ]

    result2 = solution(game_board2, table2)
    print(f"Test Case 2 Result: {result2} (Expected: 0)")

if __name__ == "__main__":
    main()