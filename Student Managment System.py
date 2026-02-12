# ----------- Student Class -----------

class Student:
    def __init__(self, roll_no, name, marks1, marks2, marks3):
        self.roll_no = roll_no
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total(self):
        return self.marks1 + self.marks2 + self.marks3

    def percentage(self):
        return self.total() / 3

    def grade(self):
        per = self.percentage()
        if per >= 90:
            return "A+"
        elif per >= 75:
            return "A"
        elif per >= 60:
            return "B"
        elif per >= 50:
            return "C"
        else:
            return "Fail"


# ----------- Report Card System -----------

class ReportCardSystem:
    def __init__(self):
        self.students = []

    # Add Student Report
    def add_student(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks1 = int(input("Enter Marks for Subject 1: "))
        marks2 = int(input("Enter Marks for Subject 2: "))
        marks3 = int(input("Enter Marks for Subject 3: "))

        student = Student(roll_no, name, marks1, marks2, marks3)
        self.students.append(student)

        print("Report added successfully!\n")

    # View All Reports
    def view_reports(self):
        if len(self.students) == 0:
            print("No reports available.\n")
            return

        for student in self.students:
            print("Roll No:", student.roll_no)
            print("Name:", student.name)
            print("Total Marks:", student.total())
            print("Percentage:", round(student.percentage(), 2))
            print("Grade:", student.grade())
            print("---------------------------")

    # Search Student Report
    def search_student(self):
        roll_no = input("Enter Roll Number to Search: ")

        for student in self.students:
            if student.roll_no == roll_no:
                print("Student Found!")
                print("Name:", student.name)
                print("Total Marks:", student.total())
                print("Percentage:", round(student.percentage(), 2))
                print("Grade:", student.grade())
                print()
                return

        print("Student not found!\n")


# ----------- Main Program -----------

def main():
    system = ReportCardSystem()

    while True:
        print("===== Student Report Card Management System =====")
        print("1. Add Student Report")
        print("2. View All Reports")
        print("3. Search Student Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_reports()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
