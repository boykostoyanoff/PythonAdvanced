rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([ch for ch in input()])

symbol = input()
is_symbol = False
for row in range(rows):
    for cow in range(rows):
        if symbol == matrix[row][cow]:
            print(f'({row}, {cow})')
            is_symbol = True
            break
    if is_symbol:
        break

if not is_symbol:
    print(f'{symbol} does not occur in the matrix')