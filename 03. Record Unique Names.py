names = set()

for _ in range(int(input())):
    name = input()
    if name not in names:
        names.add(name)

[print(name) for name in names]