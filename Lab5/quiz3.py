i = 0
counter  = 0
sum = 0
num_even = 0
num_odd = 0
num_positive = 0
num_negative = 0

while(1):
    i = input("Enter an integer or q to quit: ")
    if(i == 'q'):
        break
    i = int(i)
    counter += 1
    sum = i + sum
    if (i % 2 == 0):
        num_even += 1
    else:
        num_odd += 1
    
    if (i > 0):
        num_positive += 1
    elif (i < 0):
        num_negative += 1

print("\nSummary information: ")
print(f"You have entered {counter} integers.")
print(f"The sum of these numbers is {sum}.")
print(f"There are {num_even} even numbers.")
print(f"There are {num_odd} odd numbers.")
print(f"There are {num_positive} positive numbers.")
print(f"There are {num_negative} negative numbers.")