import sys

def pascal_triangle(rows, columns):
    # 맨 위는 항상 1
    triangle = [[1]]
    
    for _ in range(rows-1):
        new_row = [1]
        last_row = triangle[-1]
        # 범위 벗어나지 않게
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row.append(1)
        triangle.append(new_row)
        
    return triangle[rows-1][columns-1]

input = sys.stdin.readline
n,k = map(int,input().split())

print(pascal_triangle(n,k))