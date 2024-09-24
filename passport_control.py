def solution(n, times):
    answer = 0
    start = 1 
    end = max(times) * n

    # binary search의 정석
    while (start <= end):
        mid = (start + end) // 2
        
        # 모두 검사할 수 없음
        if (sum(mid // i for i in times)) < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    
    return answer

print(solution(6, [7, 10]))
