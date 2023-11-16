class Employee:
    def __init__(self, employee_id, first_name, last_name, position, phone):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.phone = phone

    def __repr__(self):
        return f"Employee('{self.employee_id}', '{self.first_name}', '{self.last_name}', '{self.position}', '{self.phone}')"

