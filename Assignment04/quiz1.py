def ask_transport_num():
    bikes = int(input("Enter the number of bikes: "))
    cars = int(input("Enter the number of cars: "))
    trucks = int(input("Enter the number of trucks: "))
    return(bikes, cars, trucks)

def display_transport(bike_num, car_num, truck_num):
    print("==========")
    print(f"Bike: {bike_num}")
    print(f"Car: {car_num}")
    print(f"Truck: {truck_num}")
    print("==========")
    

bike_num, car_num, truck_num = ask_transport_num()
display_transport(bike_num, car_num, truck_num)
