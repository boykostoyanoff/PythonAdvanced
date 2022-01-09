rows, columns = [int(i) for i in input().split(', ')]
matrix = []
total_sum = 0

for row in range(rows):
    matrix.append([int(n) for n in input().split(', ')])
    total_sum += sum(matrix[row])

print(total_sum)
print(matrix)