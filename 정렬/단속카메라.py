def solution(routes):
    # 경로를 종료 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    cameras = 0
    current_camera = -30001  # 가능한 최소 범위보다 작은 값으로 초기화
    
    for route in routes:
        # 현재 카메라가 이 경로를 커버하지 못하면 카메라 추가
        if current_camera < route[0]:
            cameras += 1
            current_camera = route[1]
    
    return cameras

# 테스트
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))  # 출력: 2