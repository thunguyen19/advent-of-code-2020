def get_input(file_name):
    store = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            store.append(line.strip())
    return store


def do_math_left_to_right(stack):
    while stack and len(stack) >= 3:
        num2 = stack.pop(0)
        operation = stack.pop(0)
        num1 = stack.pop(0)
        current = calculate(num1, num2, operation)
        stack.insert(0, current)
    return stack[-1]


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    if operation == '*':
        return num1 * num2


def get_summary(func, expressions):
    result = []
    for expression in expressions:
        result.append(func(expression))
    return sum(result)


# PART 1
def find_sum_all_expressions(expressions):

    def do_math(input_string):
        stack = []
        for char in input_string:
            if char == ' ':
                continue
            elif char == ')':
                inside_parenthesis = []
                while stack and stack[-1] != '(':
                    inside_parenthesis.insert(0, stack.pop())
                stack.pop()  # remove '('
                stack.append(do_math_left_to_right(inside_parenthesis))
            elif not char.isnumeric():
                stack.append(char)
            else:
                stack.append(int(char))
        return do_math_left_to_right(stack)

    return get_summary(do_math, expressions)


# PART 2
def find_sum_all_expressions_addition_before_multiply(expressions):

    def addition(stack, value):
        stack.pop()  # pop '+'
        current = stack.pop() + value
        stack.append(current)
        return stack

    def do_math(input_string):
        stack = []
        for char in input_string:
            if char == ' ':
                continue
            elif stack and stack[-1] == '+' and char != '(':
                stack = addition(stack, int(char))
            elif char == ')':
                inside_parenthesis = []
                while stack and stack[-1] != '(':
                    inside_parenthesis.insert(0, stack.pop())
                stack.pop()  # remove '('
                value = do_math_left_to_right(inside_parenthesis)
                if stack:
                    if stack[-1] != '+':
                        stack.append(value)
                    else:
                        stack = addition(stack, value)
                else:
                    stack.append(value)
            elif not char.isnumeric():
                stack.append(char)
            else:
                stack.append(int(char))
        return do_math_left_to_right(stack)

    return get_summary(do_math, expressions)


if __name__ == '__main__':
    data = get_input('input.txt')
    assert find_sum_all_expressions(data) == 510009915468
    assert find_sum_all_expressions_addition_before_multiply(data) == 321176691637769
