def collect_data():
    student_name = input("Enter student name: ")
    course = input("Enter course name: ")
    
    while True:
        try:
            marks = int(input("Enter marks: "))
            break
        except ValueError:
            print("Please enter a valid number")

    return {
        "student_name": student_name,
        "course": course,
        "marks": marks
    }
