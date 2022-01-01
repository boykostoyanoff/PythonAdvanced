numbers = input().split(' ')
numbers = [float(n) for n in numbers]
numbers_set = set()

for n in numbers:
    if n not in numbers_set:
        print(f'{n:.1f} - {numbers.count(n)} times')
        numbers_set.add(n)