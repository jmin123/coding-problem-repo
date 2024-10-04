def solution(n, s):
    # n이 s보다 크면 합을 s로 만들 수 없음
    if n > s:
        return [-1]
    
    base = s // n
    remainder = s % n
    
    # base가 0인 경우, n <= s가 아니라면 이미 위에서 -1을 반환
    # 그렇지 않으면 base >=1 이므로 문제 없음
    
    # 최적의 집합: 나머지를 먼저 분배하여 높은 숫자부터 채움
    result = [base] * (n - remainder) + [base + 1] * remainder
    
    return result

# 테스트 케이스
print(solution(2, 9))  # 기대 출력: [5, 4]
print(solution(2, 1))  # 기대 출력: [-1]
print(solution(2, 8))  # 기대 출력: [4, 4]
print(solution(3, 8))  # 기대 출력: [3, 3, 2]
print(solution(5, 8))  # 기대 출력: [2, 2, 2, 1, 1]
