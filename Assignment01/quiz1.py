# Input length of the box and date of birth (DOB)
box_length = int(input("Enter length of the box: "))
dob = input("Enter your dob (DD-MM-YYYY): ")

# Split the DOB into day, month, and year
day, month, year = dob.split('-')

# Define a dictionary to map numeric months to their abbreviated forms
month_dict = {
    '01': 'Jan', '02': 'Feb', '03': 'Mar',
    '04': 'Apr', '05': 'May', '06': 'Jun',
    '07': 'Jul', '08': 'Aug', '09': 'Sep',
    '10': 'Oct', '11': 'Nov', '12': 'Dec'
}

# Format the DOB
formatted_dob = f"{day}/{month_dict[month]}/{year}"

# Create a decorative border
border = "*" * box_length

# Calculate the width for the formatted DOB
dob_width = box_length - 9  # Subtracting the length of "|DOB:   |"

# Display the decorative representation of DOB with right alignment
print(border)
print(f"|DOB:   {formatted_dob:>{dob_width}}|")
print(border)   
