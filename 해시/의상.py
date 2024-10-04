def solution(clothes):
    answer = 1
    n = len(clothes)

    # clothes[i] 별로 종류를 저장
    clothe_type = dict()

    for i in range(n):
        if clothes[i][1] not in clothe_type:
            clothe_type[clothes[i][1]] = 1
        else:
            clothe_type[clothes[i][1]] += 1
    
    for i in clothe_type:
        answer *= (clothe_type[i] + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))