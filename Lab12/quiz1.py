import csv
file_name = input("Enter subject file name: ")

column_len1 = int(input("Enter 1st column length: "))
column_len2 = int(input("Enter 2nd column length: "))
column_len3 = int(input("Enter 3rd column length: "))

with open(file_name, 'r') as file:
    reader = csv.DictReader(file)

    print('Code'.ljust(column_len1) + 'Name'.center(column_len2) + 'CP'.rjust(column_len3))

        # Print subject information
    for row in reader:
        subject_code = row.get("code")
        subject_name = row.get("name")
        cp = row.get("cp")
        print(subject_code.ljust(column_len1) + subject_name.center(column_len2) + cp.rjust(column_len3))
