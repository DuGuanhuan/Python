import json

# Input subject information
subject_code = input("Enter subject code: ")
subject_title = input("Enter subject title: ")
credit_points = int(input("Number of credit points: "))
cost_per_credit_point = int(input("Cost per credit point: "))
is_core_subject = input("Is this a core subject (Y/N)? ").strip().upper()

# Calculate the total fee
total_fee = credit_points * cost_per_credit_point

# Map the core subject input to 'Y' or 'N' for JSON output
core_subject = "Y" if is_core_subject == "Y" else "N"

# Create a dictionary representing the subject information
subject_info = {
    "code": subject_code,
    "title": subject_title,
    "core": core_subject,
    "cp": credit_points,
    "fee": total_fee
}

# Convert the dictionary to JSON format
json_output = json.dumps(subject_info, indent=2)

# Display the JSON output
print("\nHere is the JSON output")
print(json_output)

