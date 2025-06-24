def student_operations():
    students = [
        ("ashwini", 20, 98, "kopargaon"),
        ("shreyash", 21, 95, "kopargaon"),
        ("kajal", 22, 99, "bendewadi"),
        ("ganubhau", 24, 89, "vaijapur")
    ]
    marks_above_90 = list(filter(lambda x: x[2] > 90, students))
    print("Students with marks above 90:", marks_above_90)
    topper = max(students, key=lambda x: x[2])
    print("Topper:", topper)
    youngest = min(students, key=lambda x: x[1])
    print("Youngest student:", youngest)
    kopargaon_students = list(filter(lambda x: x[3] == "kopargaon", students))
    print("Students from Kopargaon:", kopargaon_students)

while True:
    print("\nMenu:")
   
    print("1. Student operations")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        student_operations()
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

        