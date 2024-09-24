from itertools import combinations

def solution(relation):
    row_num = len(relation)
    col_num = len(relation[0])

    all_combi = []

    for i in range(1, col_num + 1):
        all_combi.extend(combinations(range(col_num), i))

    def check_uniqueness(combination):
        tuple_set = set()
        for row in relation:
            tuple_set.add(tuple(row[i] for i in combination))
        return len(tuple_set) == row_num
    
