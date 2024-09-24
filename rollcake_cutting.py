def solution(topping):
    answer = -1
    
    # 전체 토핑의 종류와 개수를 세는 딕셔너리를 만들자
    total_topping_dict = {}
    for t in topping:
        if t in total_topping_dict:
            total_topping_dict[t] += 1
        else:
            total_topping_dict[t] = 1
    
    # 철수의 토핑 종류를 세는 딕셔너리를 만들자
    chul_topping_dict = {}

    # 배열을 돌면서 
    for t in total_topping_dict:
        # 철수의 딕셔너리에 토핑을 넣는다
        chul_topping_dict[t] = 1
        # 전체 딕셔너리에서 토핑을 빼자
        total_topping_dict[t] -= 1
        # 철수와 동생의(전체 - 철수)의 토핑 종류가 같다면 answer += 1
        if len(chul_topping_dict) == len(total_topping_dict):
            answer += 1
    
    return answer