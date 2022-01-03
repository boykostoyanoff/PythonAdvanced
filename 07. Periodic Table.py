elements = set()
for _ in range(int(input())):
    for element in input().split(' '):
        elements.add(element)
[print(element) for element in elements]