students = []

def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if len(students) == 0:
        print("No Students Found!")
    else:
        print("\nStudent Records")
        print("-" * 30)

        for student in students:
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print("-" * 30)

def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found!")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            return

    print("Student Not Found!")

def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")