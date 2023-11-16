# class Employee:
class Employee:
    def __init__(self, employee_id, first_name, last_name, position, phone):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.phone = phone

employeeObj1 = Employee(100001, 'John', 'Lee', 'Accountant', '0001')
employeeObj2 = Employee(100002, 'Mary', 'Zheng', 'Programmer', '0002')
employeeObj3 = Employee(100003, 'Cindy', 'Wilson', 'DBA', '0001')
# employeeObj1: 100001, John, Lee, Accountant, 0001
# employeeObj2: 100002, Mary, Zheng, Programmer, 0002
# employeeObj3: 100003, Cindy, Wilson, DBA, 0001
