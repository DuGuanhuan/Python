subject_code = input("Enter subject code: ")
subject_title = input("Enter subject title: ")
credit_points = int(input("Number of credit points: "))
cost_per_credit_point = int(input("Cost per credit point: "))
is_core_subject = input("Is this a core subject (Y/N)? ")

total_fee = credit_points * cost_per_credit_point

print("\nHere is the XML output")
print(f'<?xml version="1.0"?>') 
print(f'<subject code="{subject_code}" core="{is_core_subject}">')
print(f"  <title>{subject_title}</title>")
print(f"  <cp>{credit_points}</cp>")
print(f"  <fee听过>{total_fee}</fee>")
print(f"</subject>")
