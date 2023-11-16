degree_choice = input("Which degree do you choose? Undergraduate (U) or Postgraduate (P): ")

if degree_choice == "U":
    location = "Wollongong, Liverpool"
    duration = "3 years full-time or part-time equivalent"
elif degree_choice == "P":
    course_choice = input("Which course do you choose? Master by Coursework (C) or Master by Research (R): ")
    
    if course_choice == "C":
        location = "Wollongong, Liverpool"
        duration = "1.5-2 years full-time or part-time equivalent"
    elif course_choice == "R":
        location = "Wollongong"
        duration = "2 years full-time or part-time equivalent"
    else:
        location = "Unknown"
        duration = "Unknown"
else:
    location = "Unknown"
    duration = "Unknown"

print("\nCourse summary:")
print(f"Location: {location}")
print(f"Duration: {duration}")
