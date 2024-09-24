def solution(a, b, g, s, w, t):
    left = 0
    right = 4 * 10**14  # 충분히 큰 값으로 설정

    while left <= right:
        mid = (left + right) // 2

        total_gold = 0
        total_silver = 0
        total_carrying = 0

        for i in range(len(g)):
            # 해당 시간 내에 가능한 왕복 횟수 계산
            trips = mid // (2 * t[i])
            if mid % (2 * t[i]) >= t[i]:
                trips += 1

            # 해당 트립에서 운반할 수 있는 총 무게
            max_carrying = trips * w[i]
            gold = min(g[i], max_carrying)
            silver = min(s[i], max_carrying)
            carrying = min(g[i] + s[i], max_carrying)

            total_gold += gold
            total_silver += silver
            total_carrying += carrying

        # 운반 가능 여부 확인
        if total_gold >= a and total_silver >= b and total_carrying >= a + b:
            right = mid - 1
        else:
            left = mid + 1

    return left