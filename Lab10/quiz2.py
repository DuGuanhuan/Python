# mapping from state abb to state full name
state_map = {
    "NSW": "New South Wales",
    "ACT": "Australian Capital Territory",
    "NT": "Northern Territory",
    "QLD": "Queensland",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "WA": "Western Australia"
}

# write your code here
use_input = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
print(f"The state you entered is {state_map[use_input]}")