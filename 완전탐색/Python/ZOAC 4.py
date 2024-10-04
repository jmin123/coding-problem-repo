import math

H, W, N, M = map(int, input().split())

max_rows = (H + N) // (N + 1)
max_cols = (W + M) // (M + 1)

max_participants = max_rows * max_cols

print(max_participants)
