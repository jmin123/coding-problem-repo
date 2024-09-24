import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    # 들어오는 외주 개수
    n = int(input())
    
    dp = [0] * (n + 1)
    # 들어오는 외주 개수만큼 반복
    for i in range(n):
        t, p = map(int, input().split())
        # 외주 기간이 휴가 기간을 넘지 않으면
        if i + t <= n:
            dp[i + t] = max(dp[i + t], dp[i] + p)

    print(dp[n])
