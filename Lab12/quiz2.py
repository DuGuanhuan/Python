file_name = input("Enter student file name: ")

column_len1 = int(input("Enter 1st column length: "))
column_len2 = int(input("Enter 2nd column length: "))
column_len3 = int(input("Enter 3rd column length: "))

with open(file_name, 'r') as file:
    lines = file.read().splitlines()

print('Student Number'.rjust(column_len1) + 'First Name'.rjust(column_len2) + 'Last Name'.rjust(column_len3))
for i in range(0, len(lines), 3):
    student_number = lines[i].strip().rjust(column_len1)
    first_name = lines[i + 1].strip().rjust(column_len2)
    last_name = lines[i + 2].strip().rjust(column_len3)
    print(student_number + first_name + last_name)
