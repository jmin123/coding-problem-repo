def is_operator(char):
    return char in ['+', '-', '*', '/']

def prefix_to_infix(expression):
    stack = []
    
    # Reverse the expression since we'll process it from right to left
    expression = expression.split()[::-1]
    
    for char in expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = f"({operand1} {char} {operand2})"
            stack.append(infix)
    
    return stack.pop()

# Get user input
prefix_expr = input("Enter a prefix expression (use spaces between operators and operands): ")

# Convert prefix to infix
infix_expr = prefix_to_infix(prefix_expr)

# Display results
print(f"Prefix expression: {prefix_expr}")
print(f"Infix expression: {infix_expr}")