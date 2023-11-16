print("Packaging lollies into boxes")
lollies_brand = input("Enter the lollies brand: ")
num_lollies = int(input("Enter number of lollies: "))
lollies_per_box = int(input("How many lollies in 1 box? "))

num_boxes_needed = num_lollies // lollies_per_box
lollies_left_over = num_lollies % lollies_per_box

print(f"{lollies_brand} lollies packaging calculation")
print(f"Number of lollies: {num_lollies}")
print(f"Number of lollies per box: {lollies_per_box}")
print(f"Number of boxes needed: {num_boxes_needed}")
print(f"Number of lollies left over: {lollies_left_over}")
