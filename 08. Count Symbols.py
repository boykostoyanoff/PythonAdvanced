text = input()
unique_characters = set()
[unique_characters.add(ch) for ch in text]
[print(f'{ch}: {text.count(ch)} time/s') for ch in sorted(list(unique_characters))]