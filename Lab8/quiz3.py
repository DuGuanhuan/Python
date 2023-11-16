class Staff:
    def __init__(self, staff_number, first_name, last_name, email):
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print_details(self, width):
        # Calculate the length of the lines and spaces
        line_length = width - 4

        # Print the top border
        print('-' * width)

        # Print the staff number line
        print(f"| Staff number: {self.staff_number.ljust(line_length - 14)} |")

        # Print the name line
        full_name = f"{self.first_name} {self.last_name}"
        print(f"| {full_name.ljust(line_length)} |")

        # Print the email line
        print(f"| {self.email.ljust(line_length)} |")

        # Print the bottom border
        print('-' * width)

# Create a Staff object
staffObj = Staff("012345", "John", "Smith", "js@gmail.com")

# Print details with width 40
staffObj.print_details(40)
