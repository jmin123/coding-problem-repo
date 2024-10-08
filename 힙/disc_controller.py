import heapq

def solution(jobs):
    # 작업을 요청 시간 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    heap = []
    index = 0
    current_time = 0
    total_waiting_time = 0
    n = len(jobs)
    
    while index < n or heap:
        # 현재 시간에 도착한 모든 작업을 힙에 추가
        while index < n and jobs[index][0] <= current_time:
            heapq.heappush(heap, (jobs[index][1], jobs[index][0]))  # (처리 시간, 요청 시간)
            index += 1
        
        if heap:
            processing_time, request_time = heapq.heappop(heap)
            current_time += processing_time
            total_waiting_time += current_time - request_time
        else:
            # 힙이 비어있다면, 다음 작업의 요청 시간으로 시간을 이동
            if index < n:
                current_time = jobs[index][0]
    
    average_waiting_time = total_waiting_time // n
    return average_waiting_time

# 테스트 케이스 실행
print(solution([[5, 10], [6, 8], [11, 5], [14, 2], [100, 7]]))  # 예상 출력: 11