rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(n) for n in input().split(', ')])

result = []
[result.extend(row) for row in matrix]
print(result)