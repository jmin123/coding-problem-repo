from itertools import permutations

def solution(numbers):
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    answer = 0

    nums = set()

    for i in range(len(numbers)):
        nums.update(map(int, map(''.join, permutations(numbers, i + 1))))

    print(nums)
    for num in nums:
        if is_prime(num) and num > 1:
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))