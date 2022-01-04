odd_set = set()
even_set = set()

for row in range(int(input())):
    name = input()
    sum_of_ascii = sum(ord(ch) for ch in name)
    result = sum_of_ascii // (row + 1)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    result = odd_set.intersection(even_set)
elif odd_sum > even_sum:
    result = odd_set
else:
    result = even_set.union(odd_set)
result = list(result)
for i in range(len(result) - 1):
    print(result[i], end=', ')
print(result[-1])