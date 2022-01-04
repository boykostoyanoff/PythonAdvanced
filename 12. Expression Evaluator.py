string_expression = input().split(' ')
elements_to_calculate = []
result = int(string_expression.pop(0))

while string_expression:
    current_element = string_expression.pop(0)
    if current_element == '+':
        result += sum(elements_to_calculate)
        elements_to_calculate = []
    elif current_element == '-':
        while elements_to_calculate:
            result -= elements_to_calculate.pop(0)
        elements_to_calculate = []
    elif current_element == '*':
        while elements_to_calculate:
            result *= elements_to_calculate.pop(0)
        elements_to_calculate = []
    elif current_element == '/':
        while elements_to_calculate:
            result = int(result / elements_to_calculate.pop(0))
        elements_to_calculate = []
    else:
        elements_to_calculate.append(int(current_element))

print(result)