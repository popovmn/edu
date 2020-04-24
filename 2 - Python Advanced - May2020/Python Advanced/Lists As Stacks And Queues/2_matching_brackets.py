# def mb(exp):
#     temp_start_index = []
#     expressions = []
#     for i in range(len(exp)):
#         char = exp[i]
#         if char == "(":
#             temp_start_index.append(i)
#         elif char == ")":
#             start = temp_start_index.pop()
#             end = i
#             expressions.append(exp[start:end + 1])
#     return expressions
#
#
# if __name__ == "__main__":
#     [print(e) for e in mb(input())]


def foo(expression):
    result = []
    temp = []
    for i in range(len(expression)):
        if expression[i] == "(":
            temp.append(i)
        if expression[i] == ")":
            start = temp.pop()
            end = i
            result.append(expression[start:end + 1])
    return result


exp = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
if __name__ == "__main__":
    [print(e) for e in foo(exp)]
