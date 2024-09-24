"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

- 제한 조건 -
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""

def solution(arr1, arr2):
    arr2_transposed = list(zip(*arr2))
    print(arr2_transposed)

    result = [
        [sum(a * b for a, b in zip(row, col)) for col in arr2_transposed]
        for row in arr1
    ]

    return result

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))