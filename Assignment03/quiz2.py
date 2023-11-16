student_id = input("Enter a student id: ")
start_num = int(input("Enter a starting number: "))
num_equations = int(input("Enter number of equations: "))

print("Equation display:")
for i in range(num_equations):
    print(f"{student_id} + {start_num + i} = {int(student_id) + (start_num + i)}")
