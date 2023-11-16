# Define the Staff class
class Staff:
    def __init__(self, staff_number, first_name, last_name, email):
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

# Create Staff objects
staffObj1 = Staff(100001, 'John', 'Lee', 'jl123@gmail.com')
staffObj2 = Staff(100002, 'Mary', 'Zheng', 'maryz@gmail.com')
staffObj3 = Staff(100003, 'Cindy', 'Wilson', 'cw456@hotmail.com')
