first_line = input().split(' ')
first_line = {int(x) for x in first_line}

second_line = input().split(' ')
second_line = {int(x) for x in second_line}

for i in range(int(input())):
    command = input().split(' ')
    action = f'{command[0]} {command[1]}'
    line = {int(x) for x in command[2:]}

    if action == 'Add First':
        first_line = first_line.union(line)
    elif action == 'Add Second':
        second_line = second_line.union(line)
    elif action == 'Remove First':
        first_line = first_line.difference(line)
    elif action == 'Remove Second':
        second_line = second_line.difference(line)
    else:
        print(first_line.issubset(second_line) or second_line.issubset(first_line))

first_line = sorted(list(first_line))
for _ in range(len(first_line)):
    if _ == len(first_line) - 1:
        print(first_line[-1])
    else:
        print(first_line[_], end=', ')

second_line = sorted(list(second_line))
for _ in range(len(second_line)):
    if _ == len(second_line) - 1:
        print(second_line[-1])
    else:
        print(second_line[_], end=', ')