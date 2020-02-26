import random
# Each traffic light starts with a random number of cars.
fanari1 = random.randint(1,25)
print("Fanari1 has currently ", fanari1," cars")
fanari2 = random.randint(1,25)
print("Fanari2 has currently ", fanari2," cars")
fanari3 = random.randint(1,25)
print("Fanari3 has currently ", fanari3," cars\n")
while fanari1 > 0 and fanari2 > 0 and fanari3 > 0: # This loop will stop only if one or more traffic lights have zero cars.
    max = fanari1
    if max <= fanari2: # Checks if max is smaller or equal than fanari2
        if max == fanari2: # Checks if its equal then we choose randomly the value of max between max(the value that it currently has) and fanari2
            rand_fanari = random.randint(0,1)
            if rand_fanari == 1:
                max = fanari2
        else:
            max = fanari2

    if max <= fanari3: # Checks if max is smaller or equal than fanari3
        if max == fanari3: # Checks if its equal then we choose randomly the value of max between max(the value that it currently has) and fanari3
            rand_fanari = random.randint(0,1)
            if rand_fanari == 1:
                max = fanari3
        else:
            max = fanari3

    if max == fanari1: # Checks if fanari1 is green. If it is then we add a random number of cars and we substract a random number of cars from the other traffic lights.
        less_cars = random.randint(5,10)
        fanari1 -= less_cars
        print("\nFanari1 is green and the number of cars that left Fanari1 were ", less_cars)
        if fanari1 >= 0:
            print("Fanari1 has ", fanari1, " cars")
        else:
            print("Fanari1 has ", 0, " cars")
        more_cars = random.randint(0,5)
        print("The number of cars that they came to Fanari2 are: ", more_cars)
        fanari2 += more_cars
        more_cars = random.randint(0,5)
        print("The number of cars that they came to Fanari3 are: ", more_cars)
        fanari3 += more_cars

    elif max == fanari2: # Checks if fanari2 is green. If it is then we add a random number of cars and we substract a random number of cars from the other traffic lights.
        less_cars = random.randint(5,10)
        fanari2 -= less_cars
        print("\nFanari2 is green and the number of cars that left were ", less_cars)
        if fanari2 >= 0:
            print("Fanari2 has ", fanari2, " cars")
        else:
            print("Fanari2 has ", 0, " cars")
        more_cars = random.randint(0,5)
        print("The number of cars that they came to Fanari1 are: ", more_cars)
        fanari1 += more_cars
        more_cars = random.randint(0,5)
        print("The number of cars that they came to Fanari3 are: ", more_cars)
        fanari3 += more_cars

    else: # Checks if fanari3 is green. If it is then we add a random number of cars and we substract a random number of cars from the other traffic lights.
        less_cars = random.randint(5,10) 
        fanari3 -= less_cars
        print("\nFanari3 is green and the number of cars that left were ", less_cars)
        if fanari3 >= 0:
            print("Fanari3 has ", fanari3, " cars")
        else:
            print("Fanari3 has ", 0, " cars")
        more_cars = random.randint(0,5)
        print("The number of cars that they came to Fanari1 are: ", more_cars)
        fanari1 += more_cars
        more_cars = random.randint(0,5)
        print("The number of cars that they came to Fanari2 are: ", more_cars)
        fanari2 += more_cars
