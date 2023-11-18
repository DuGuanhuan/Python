def math_expression_checking(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or brackets[char] != stack.pop():
                return False

    return not stack
