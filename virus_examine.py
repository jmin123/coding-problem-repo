if __name__ == "__main__":
    answer = 0
    restaurant = int(input())
    customer = list(map(int, input().split()))  # Read all customer data in one line
    # 팀장 및 팀원 한 명이 검사 가능한 최대 고객 수
    team_leader, team_member = map(int, input().split())

    for i in range(restaurant):
        if customer[i] <= team_leader:  # Compare directly with the customer value
            answer += 1
        elif customer[i] > team_leader:
            temp = customer[i] - team_leader
            # 팀장이 할당량만큼 검사하고, 팀원들이 나머지 손님들을 검사해야 한다
            if temp % team_member == 0:
                answer += temp // team_member
            # 딱 나누어 떨어지지 않으면 한 명이 더 필요
            else:
                answer += temp // team_member + 1
            # 팀장까지 포함해서 검사해야 하므로 +1
            
    print(answer)
