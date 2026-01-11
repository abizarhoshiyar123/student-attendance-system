import datetime

students_file = "students.txt"
attendance_file = "attendance.txt"

def add_student():
    name = input("Enter student name: ")
    with open(students_file, "a") as f:
        f.write(name + "\n")
    print(f"{name} added successfully!\n")

def view_students():
    print("\nRegistered Students:")
    try:
        with open(students_file, "r") as f:
            students = f.readlines()
            for s in students:
                print("- ", s.strip())
    except FileNotFoundError:
        print("No students found.\n")

def mark_attendance():
    date = datetime.date.today()
    print(f"\nAttendance for {date}")
    
    try:
        with open(students_file, "r") as f:
            students = [s.strip() for s in f.readlines()]
    except FileNotFoundError:
        print("No students found. Add students first.\n")
        return

    with open(attendance_file, "a") as f:
        for student in students:
            status = input(f"{student} (P/A): ").upper()
            if status not in ["P", "A"]:
                status = "A"
            f.write(f"{date},{student},{status}\n")

    print("\nAttendance saved!\n")

def view_attendance():
    print("\nAttendance Records:")
    try:
        with open(attendance_file, "r") as f:
            records = f.readlines()
            for r in records:
                date, name, status = r.strip().split(",")
                print(f"{date} - {name}: {'Present' if status=='P' else 'Absent'}")
        print()
    except FileNotFoundError:
        print("No records found.\n")

def main():
    while True:
        print("===== Attendance System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
