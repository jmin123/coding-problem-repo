def generateParenthesis(n):
    def backtrack(current_string, open_count, close_count):
        if len(current_string) == 2 * n:
            result.append(current_string)
            return
        
        if open_count < n:
            backtrack(current_string + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current_string + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result

n = 3
print(generateParenthesis(n))