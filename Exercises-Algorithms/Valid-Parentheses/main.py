def is_Valid(s):
    # We'll use a stack like structure where we'll put every open parenthesis
    # Once we encounter a closing parenthesis, we'll search for the latest open parenthesis of that kind
    # Once we find it, we'll pop it from the stack
    # The expression is correct if at the end the stack is empty
    if len(s) == 1:
        return False

    stack = []
    open_parenthesis = ['(', '[', '{']

    for element in s:
        if element in open_parenthesis:
            stack.append(element)
        else:
            if len(stack) == 0:
                return False

            length = len(stack) - 1

            if element == ')':
                looking_for = '('
            elif element == ']':
                looking_for = '['
            else:
                looking_for = '{'

            while length >= 0:
                if looking_for == stack[length]:
                    del stack[length]
                    break
                else:
                    return False

    if len(stack) == 0:
        return True

    return False


s1 = ")(){}"
print(is_Valid(s1))
