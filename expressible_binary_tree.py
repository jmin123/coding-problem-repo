def solution(numbers):
    def is_complete_binary_tree(s):
        if len(s) == 1:
            return s == '1'
        
        mid = len(s) // 2
        left_subtree = s[:mid]
        right_subtree = s[mid+1:]
        
        if s[mid] == '0':
            return all(bit == '0' for bit in left_subtree) and all(bit == '0' for bit in right_subtree)
        
        return is_complete_binary_tree(left_subtree) and is_complete_binary_tree(right_subtree)
    
    def check_binary_tree(n):
        s = bin(n)[2:]
        N = len(s)
        target_length = 2**((N-1).bit_length()) - 1
        s = '0' * (target_length - N) + s
        
        return is_complete_binary_tree(s)
    
    return [1 if check_binary_tree(n) else 0 for n in numbers]