def solution(info, edges):
    def dfs(sheep, wolf, current, available):
        nonlocal max_sheep # 최대 양의 수

        # 만약 양이 늑대와 같아져버리거나 늑대가 더 많아지면 돌아가기
        if sheep <= wolf:
            return
        
        max_sheep = max(max_sheep, sheep) # 최대 양의 수 갱신

        for next_node in available:
            new_available = available.copy() # 얕은 복사
            new_available.remove(next_node)
            new_available.extend([child for parent, child in edges if parent == next_node])

            if info[next_node] == 0: # 만약 현재 노드가 양이라면
                dfs(sheep + 1, wolf, next_node, new_available)
            else: # 만약 현재 노드가 늑대라면
                dfs(sheep, wolf + 1, next_node, new_available)

    max_sheep = 0
    dfs(1, 0, 0, [child for parent, child in edges if parent == 0]  )
    return max_sheep