def find_bike_car_truck(wheel):
    found = False
    for Bike in range(1, int(wheel / 2) + 1):
        for Car in range(0, int(wheel / 4) + 1):
            for Truck in range(0, int(wheel / 8) + 1):
                if((2 * Bike + 4 * Car + 8 * Truck) == wheel):
                    print(f"Bike: {Bike}, Car: {Car}, Truck: {Truck}")  
                    found = True
    if not found:
        print("Not found")  # 如果没有找到符合条件的组合，输出 "Not found"

    
find_bike_car_truck(6)