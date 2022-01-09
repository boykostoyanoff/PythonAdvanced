rows = int(input())
matrix = []
primary_diagonal_sum = 0

for row in range(rows):
    matrix.append([n for n in input().split(' ')])
    primary_diagonal_sum += int(matrix[row][row])

print(primary_diagonal_sum)