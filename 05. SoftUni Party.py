number_of_guest = int(input())
reservation_codes = set()

for _ in range(number_of_guest):
    reservation_codes.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        if guest in reservation_codes:
            reservation_codes.remove(guest)

print(len(reservation_codes))
[print(guest) for guest in list(sorted(reservation_codes))]