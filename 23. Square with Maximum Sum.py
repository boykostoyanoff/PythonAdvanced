rows, cows = [int(n) for n in input().split(', ')]
matrix = []
result = []
max_sum = 0

for row in range(rows):
    matrix.append([int(n) for n in input().split(', ')])

for row in range(rows - 1):
    for cow in range(cows -1):
        c_sum = matrix[row][cow] + matrix[row][cow + 1] + matrix[row + 1][cow] + matrix[row + 1][cow + 1]
        if c_sum > max_sum:
            max_sum = c_sum
            result = [[matrix[row][cow], matrix[row][cow + 1]], [matrix[row + 1][cow], matrix[row + 1][cow + 1]]]

for row in result:
    print(' '.join([str(x) for x in row]))
print(max_sum)
