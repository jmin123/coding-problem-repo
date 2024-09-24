from itertools import product

def is_match(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True

def solution(user_id, banned_id):
    # 1. 각 불량 사용자 ID와 일치하는 실제 사용자 ID 찾기
    matched_users = []
    for banned in banned_id:
        matched = [user for user in user_id if is_match(user, banned)]
        matched_users.append(matched)
    
    # 2. 가능한 모든 조합 만들기
    all_combinations = product(*matched_users)
    # 3. 중복 제거 및 유효한 조합 세기
    valid_combinations = set()  
    for combo in all_combinations:
        if len(set(combo)) == len(banned_id):  # 중복된 사용자가 없는 경우만
            valid_combinations.add(tuple(sorted(combo)))
    
    return len(valid_combinations)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))