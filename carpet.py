def solution(brown, yellow):
    brown_plus_yellow = brown + yellow

    x = 0
    for y in range(3, brown_plus_yellow):
        if brown_plus_yellow % y == 0:
            x = brown_plus_yellow // y

        if (x * 2) + (y * 2) - 4 == brown:
            return [x, y]
        
print(solution(24, 24))
print(solution(12, 4))