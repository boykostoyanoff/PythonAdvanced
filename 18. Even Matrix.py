rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(n) for n in input().split(', ') if int(n) % 2 == 0])

print(matrix)