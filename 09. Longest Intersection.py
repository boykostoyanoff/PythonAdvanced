def set_from_string(indexes_info: str):
    indexes_info = indexes_info.split(',')
    start_index = int(indexes_info[0])
    end_index = int(indexes_info[1])
    result = {x for x in range(start_index, end_index + 1)}
    return result


longest_intersection = []

for _ in range(int(input())):
    ranges_info = input().split('-')
    first_range = set_from_string(ranges_info[0])
    second_range = set_from_string(ranges_info[1])
    current_intersection = first_range.intersection(second_range)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = set(current_intersection)

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')