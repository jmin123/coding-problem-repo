def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                count += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return count

n = int(input())

classes = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    count = insertion_sort(classes[i][1:])
    
    print(i + 1, count)