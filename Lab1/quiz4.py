price_under6 = 0
price_6to17 = 7
price_adult = 20

print("Welcome to Ocean World.")
under6 = int(input("How many tickets for children under 6? "))  # 2
sixto17 = int(input("How many tickets for children age between 6-17? "))  # 3
adult = int(input("How many tickets for adults? "))  # 2

total_cost = sixto17 * price_6to17 + adult * price_adult
num_ticket = under6 + sixto17 + adult
print("Receipt:")
print("Number of tickets:", num_ticket)
print("Total cost " + "$" + str(total_cost))
