def add_elements_to_set(empty_set: set, number_of_elements):
    for _ in range(int(number_of_elements)):
        empty_set.add(input())
    return empty_set


first_set = set()
second_set = set()

n, m = input().split(' ')

first_set = add_elements_to_set(first_set, n)
second_set = add_elements_to_set(second_set, m)

result = first_set.intersection(second_set)

for element in result:
    print(element)