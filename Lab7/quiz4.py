class Employee:
    def __init__(self, employee_id, first_name, last_name, position, phone):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.phone = phone

    def __str__(self):
        return f"{self.employee_id} {self.first_name} {self.last_name}"
