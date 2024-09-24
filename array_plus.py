def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr_num = []
        for j in range(len(arr2[0])):  # Changed to len(arr2[0]) for correct inner loop size
            arr_num.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_num)
            
    return answer