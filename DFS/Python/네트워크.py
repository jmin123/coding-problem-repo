def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(node):
        nonlocal answer

        for i in range(n):
           # 노드가 연결되어 있고 방문하지 않았으면
           if computers[node][i] == 1 and visited[i] == False:
               visited[i] = True
               dfs(i)
               
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

