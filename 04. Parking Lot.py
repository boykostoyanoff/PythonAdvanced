cars_in_garage = set()
for _ in range(int(input())):
    car_info = input().split(', ')
    if car_info[0] == 'IN':
        cars_in_garage.add(car_info[1])
    else:
        cars_in_garage.remove(car_info[1])
if cars_in_garage:
    [print(car) for car in cars_in_garage]
else:
    print('Parking Lot is Empty')