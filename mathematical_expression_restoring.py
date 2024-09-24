'''
문제 설명
당신은 덧셈 혹은 뺄셈 수식이 여러 개 적힌 고대 문명의 유물을 찾았습니다. 이 수식들을 관찰하던 당신은 이 문명이 사용하던 진법 체계가 10진법이 아니라는 것을 알아냈습니다. (2 ~ 9진법 중 하나입니다.)

수식들 중 몇 개의 수식은 결괏값이 지워져 있으며, 당신은 이 문명이 사용하던 진법에 맞도록 지워진 결괏값을 채워 넣으려 합니다.

다음은 그 예시입니다.

<수식>

14 + 3 = 17
13 - 6 = X
51 - 5 = 44
X로 표시된 부분이 지워진 결괏값입니다.
51 - 5 = 44에서 이 문명이 사용하던 진법이 8진법임을 알 수 있습니다. 따라서 13 - 6 = X의 지워진 결괏값을 채워 넣으면 13 - 6 = 5가 됩니다.

다음은 또 다른 예시입니다.

<수식>

1 + 1 = 2
1 + 3 = 4
1 + 5 = X
1 + 2 = X
주어진 수식들에서 이 문명에서 사용한 진법이 6 ~ 9진법 중 하나임을 알 수 있습니다.
1 + 5 = X의 결괏값은 6진법일 때 10, 7 ~ 9진법일 때 6이 됩니다. 이와 같이 결괏값이 불확실한 수식은 ?를 사용해 1 + 5 = ?와 같이 결괏값을 채워 넣습니다.
1 + 2 = X의 결괏값은 6 ~ 9진법에서 모두 3으로 같습니다. 따라서 1 + 2 = X의 지워진 결괏값을 채워 넣으면 1 + 2 = 3이 됩니다.

덧셈 혹은 뺄셈 수식들이 담긴 1차원 문자열 배열 expressions가 매개변수로 주어집니다. 이때 결괏값이 지워진 수식들의 결괏값을 채워 넣어 순서대로 문자열 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

제한사항
2 ≤ expressions의 길이 ≤ 100
expressions의 원소는 "A + B = C" 혹은 "A - B = C" 형태의 문자열입니다. A, B, C와 연산 기호들은 공백 하나로 구분되어 있습니다.
A, B는 음이 아닌 두 자릿수 이하의 정수입니다.
C는 알파벳 X 혹은 음이 아닌 세 자릿수 이하의 정수입니다. C가 알파벳 X인 수식은 결괏값이 지워진 수식을 의미하며, 이러한 수식은 한 번 이상 등장합니다.
결괏값이 음수가 되거나 서로 모순되는 수식은 주어지지 않습니다.
입출력 예
expressions	result
["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]	["13 - 6 = 5"]
["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]	["1 + 5 = ?", "1 + 2 = 3"]
["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]	["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]
["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]	["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]
["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]	["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

문제 예시와 같습니다.

입출력 예 #3

30 + 31 = 101에서 이 문명이 사용하던 진법이 6진법임을 알 수 있습니다. 따라서 10 - 2 = X, 3 + 3 = X, 33 + 33 = X의 지워진 결괏값을 채워 넣으면 10 - 2 = 4, 3 + 3 = 10, 33 + 33 = 110이 됩니다.

따라서 ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]을 return 해야 합니다.

입출력 예 #4

수식에 등장하는 숫자들을 통해 이 문명이 사용하던 진법이 8진법 혹은 9진법임을 알 수 있습니다. 2 + 2 = X와 5 - 5 = X의 지워진 결괏값을 채워 넣으면 8진법, 9진법에 관계없이 2 + 2 = 4, 5 - 5 = 0이 됩니다. 7 + 4 = X의 결괏값은 불확실하므로 지워진 결괏값을 채워 넣으면 7 + 4 = ?가 됩니다.

따라서 ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]을 return 해야 합니다.

입출력 예 #5

네 번째 예시와 같지만 5 - 5 = X가 8 + 4 = X로 바뀌었습니다. 이 문명이 사용하던 진법이 9진법임을 알 수 있으므로 7 + 4 = X와 8 + 4 = X의 지워진 결괏값을 채워 넣으면 7 + 4 = 12, 8 + 4 = 13이 됩니다.

따라서 ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]을 return 해야 합니다.
'''
def solution(expressions):
    def to_decimal(num_str, base):
        """Convert a number string from a given base to decimal."""
        return int(num_str, base)

    def is_valid_expression(expr, base):
        """Check if a fully defined expression is valid in the given base."""
        try:
            parts = expr.split()
            A, op, B, _, C = parts
            # Ensure all digits in A, B, and C are valid in the base
            for num in [A, B, C]:
                for digit in num:
                    if digit.isdigit() and int(digit) >= base:
                        return False
            A_dec = to_decimal(A, base)
            B_dec = to_decimal(B, base)
            C_dec = to_decimal(C, base)
            if op == '+':
                return A_dec + B_dec == C_dec
            elif op == '-':
                return A_dec - B_dec == C_dec
            else:
                return False
        except:
            return False

    def are_digits_valid(expr, base):
        """Ensure that all digits in A and B are valid in the given base for incomplete expressions."""
        try:
            parts = expr.split()
            A, op, B, _, C = parts
            # Only check A and B for incomplete expressions (C == 'X')
            for num in [A, B]:
                for digit in num:
                    if digit.isdigit() and int(digit) >= base:
                        return False
            return True
        except:
            return False

    def get_possible_bases(expressions):
        """Determine all possible bases that satisfy all expressions."""
        possible_bases = []
        for base in range(2, 10):
            valid = True
            for expr in expressions:
                parts = expr.split()
                C = parts[4]
                if C != 'X':
                    if not is_valid_expression(expr, base):
                        valid = False
                        break
                else:
                    if not are_digits_valid(expr, base):
                        valid = False
                        break
            if valid:
                possible_bases.append(base)
        return possible_bases

    def compute_missing(expr, base):
        """Compute the missing result for a given expression and base."""
        parts = expr.split()
        A, op, B, _, _ = parts
        A_dec = to_decimal(A, base)
        B_dec = to_decimal(B, base)
        if op == '+':
            result = A_dec + B_dec
        else:
            result = A_dec - B_dec
        # Convert result back to the base
        if result == 0:
            return '0'
        digits = []
        while result > 0:
            digits.append(str(result % base))
            result = result // base
        return ''.join(digits[::-1])

    possible_bases = get_possible_bases(expressions)
    incomplete_expressions = [expr for expr in expressions if expr.split()[4] == 'X']
    result = []

    for expr in incomplete_expressions:
        computed_values = set()
        uncertain = False
        for base in possible_bases:
            try:
                value = compute_missing(expr, base)
                computed_values.add(value)
                if len(computed_values) > 1:
                    uncertain = True
                    break
            except ValueError:
                # Skip bases where digits are invalid in incomplete expressions
                continue
        parts = expr.split()
        A, op, B, _, _ = parts
        if uncertain or len(computed_values) == 0:
            result.append(f"{A} {op} {B} = ?")
        else:
            result.append(f"{A} {op} {B} = {computed_values.pop()}")

    return result

print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))