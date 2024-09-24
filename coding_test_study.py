'''
당신은 코딩 테스트를 준비하기 위해 공부하려고 합니다. 코딩 테스트 문제를 풀기 위해서는 알고리즘에 대한 지식과 코드를 구현하는 능력이 필요합니다.

알고리즘에 대한 지식은 알고력, 코드를 구현하는 능력은 코딩력이라고 표현합니다. 알고력과 코딩력은 0 이상의 정수로 표현됩니다.

문제를 풀기 위해서는 문제가 요구하는 일정 이상의 알고력과 코딩력이 필요합니다.

예를 들어, 당신의 현재 알고력이 15, 코딩력이 10이라고 가정해보겠습니다.

A라는 문제가 알고력 10, 코딩력 10을 요구한다면 A 문제를 풀 수 있습니다.
B라는 문제가 알고력 10, 코딩력 20을 요구한다면 코딩력이 부족하기 때문에 B 문제를 풀 수 없습니다.
풀 수 없는 문제를 해결하기 위해서는 알고력과 코딩력을 높여야 합니다. 알고력과 코딩력을 높이기 위한 다음과 같은 방법들이 있습니다.

알고력을 높이기 위해 알고리즘 공부를 합니다. 알고력 1을 높이기 위해서 1의 시간이 필요합니다.
코딩력을 높이기 위해 코딩 공부를 합니다. 코딩력 1을 높이기 위해서 1의 시간이 필요합니다.
현재 풀 수 있는 문제 중 하나를 풀어 알고력과 코딩력을 높입니다. 각 문제마다 문제를 풀면 올라가는 알고력과 코딩력이 정해져 있습니다.
문제를 하나 푸는 데는 문제가 요구하는 시간이 필요하며 같은 문제를 여러 번 푸는 것이 가능합니다.
당신은 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하려 합니다.

초기의 알고력과 코딩력을 담은 정수 alp와 cop, 문제의 정보를 담은 2차원 정수 배열 problems가 매개변수로 주어졌을 때, 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 return 하도록 solution 함수를 작성해주세요.

제한 사항 :
제한사항
초기의 알고력을 나타내는 alp와 초기의 코딩력을 나타내는 cop가 입력으로 주어집니다.
0 ≤ alp,cop ≤ 150
1 ≤ problems의 길이 ≤ 100
problems의 원소는 [alp_req, cop_req, alp_rwd, cop_rwd, cost]의 형태로 이루어져 있습니다.
alp_req는 문제를 푸는데 필요한 알고력입니다.
0 ≤ alp_req ≤ 150
cop_req는 문제를 푸는데 필요한 코딩력입니다.
0 ≤ cop_req ≤ 150
alp_rwd는 문제를 풀었을 때 증가하는 알고력입니다.
0 ≤ alp_rwd ≤ 30
cop_rwd는 문제를 풀었을 때 증가하는 코딩력입니다.
0 ≤ cop_rwd ≤ 30
cost는 문제를 푸는데 드는 시간입니다.
1 ≤ cost ≤ 100
'''
def solution(alp, cop, problems):
    # 문제에서 요구하는 최대 문제해결 값
    max_alp_req = max(p[0] for p in problems) if alp < max([p[0] for p in problems]) else alp
    max_cop_req = max([p[1] for p in problems]) if cop < max([p[1] for p in problems]) else cop
    
    # 최소값을 구하는 거니까 inf
    dp = [[float('inf')] * (max_cop_req + 1) for _ in range(max_alp_req+1)]
    
    # 초기값
    dp[alp][cop] = 0
    
    for cur_alp in range(alp, max_alp_req+1):
        for cur_cop in range(cop, max_cop_req+1):
            # 단순히 알고력과 코딩력을 시간을 들여서 올리는 경우
            if cur_alp < max_alp_req:
                dp[cur_alp+1][cur_cop] = min(dp[cur_alp+1][cur_cop], dp[cur_alp][cur_cop] + 1)
            if cur_cop < max_cop_req:
                dp[cur_alp][cur_cop+1] = min(dp[cur_alp][cur_cop+1], dp[cur_alp][cur_cop] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 문제가 요구하는 최소 값을 충족한다면
                if cur_alp >= alp_req and cur_cop >= cop_req:
                    next_alp = min(cur_alp + alp_rwd, max_alp_req)
                    next_cop = min(cur_cop + cop_rwd, max_cop_req)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[cur_alp][cur_cop] + cost)
    return dp[max_alp_req][max_cop_req]
print(solution(10, 10, [[10,15,2,1,2], [20,20,3,3,4]]))