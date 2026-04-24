# 🧩 Task 1: Student System
class Student:
    school_name = "XYZ School"

    def set_details(self):
        self.name = "Vamsi"
        self.marks = 85

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School Name:", self.school_name)


# 👉 Outside the class:
s = Student()
s.set_details()
s.display()


# 🧩 Task 2: Employee System
class Employee:
    company = "Infosys"

    def set_data(self):
        self.name = "Ravi"
        self.salary = 20000

    def increase_salary(self):
        self.salary += 5000

    def display(self):
        print("Company:", self.company)
        print("Name:", self.name)
        print("Salary:", self.salary)


# 👉 Outside the class:
e = Employee()
e.set_data()
e.increase_salary()
e.display()

