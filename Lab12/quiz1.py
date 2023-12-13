import csv

def read_and_display_file():
    # Get user input
    file_name = input("Enter subject file name: ")
    col1_width = int(input("Enter 1st column length: "))
    col2_width = int(input("Enter 2nd column length: "))
    col3_width = int(input("Enter 3rd column length: "))

    try:
        # Open and read the CSV file
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Print the header with specified column widths and alignment
            header_format = "{:<{col1_width}}{:^{col2_width}}{:>{col3_width}}"
            row_format = "{:<{col1_width}}{:^{col2_width}}{:>{col3_width}}"
            print(header_format.format("Code", "Name", "CP", col1_width=col1_width, col2_width=col2_width, col3_width=col3_width))
            
            # Print each row with specified column widths and alignment
            for row in reader:
                print(row_format.format(row['code'], row['name'], row['cp'], col1_width=col1_width, col2_width=col2_width, col3_width=col3_width))

    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
read_and_display_file()
