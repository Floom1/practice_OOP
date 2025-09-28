from Car import Car
from CarPark import CarPark

cars = []
with open("carpark/in.txt", "r") as f:
    try:
        for line in f:
            parts = line.strip().split(" ")
            if len(parts) == 2:
                car = Car(parts[0], parts[1])
                cars.append(car)
    except Exception as e:
        print(f"Oops: {e}")


carsp = []
with open("carpark/in2.txt", "r") as f:
    try:
        for line in f:
            parts = line.strip().split(" ")
            if len(parts) == 1:
                carp = CarPark(parts[0])
                carsp.append(carp)
    except Exception as e:
        print(f"Oops: {e}")


print(carsp[0], carsp[0] == carsp[1])

carsp[0] += cars[0]
print(carsp[0], carsp[0] == carsp[1])

carsp[1] += cars[3]
print(carsp[0], "\n", carsp[1], carsp[0] == carsp[1])

carsp[0] += cars[1]
carsp[0] += cars[2]
print(carsp[0], carsp[0] == carsp[1])

with open("carpark/out.txt", "w", encoding="UTF-8") as f:
    try:
        for carp in carsp:
            f.write(str(carp) + "\n")
    except Exception as e:
        print(f"Oops: {e}")
