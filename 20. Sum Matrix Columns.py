rows, cows = [int(n) for n in input().split(', ')]
matrix = []

for row in range(rows):
    matrix.append([int(n) for n in input().split(' ')])

for cow in range(cows):
    cow_sum = 0
    for row in range(rows):
        cow_sum += matrix[row][cow]
    print(cow_sum)