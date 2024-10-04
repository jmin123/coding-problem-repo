one, two, three = map(int, input().split())

while one != 0 and two != 0 and three != 0:
    max_num = max(one, two, three)
    # 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 크면
    if max_num >= one + two + three - max_num:
        print("Invalid")
    # 세 변의 길이가 모두 같은 경우
    elif one == two == three:
        print("Equilateral")
    # 두 변의 길이가 같은 경우
    elif one == two or two == three or one == three:
        print("Isosceles")
    # 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")
    one, two, three = map(int, input().split())