#Question:
#Create a class Student with:
#Class variable: school_name = "XYZ School"
#A method set_details()
 #→ inside method, assign:
#name = "Vamsi"
#marks = 85
#A method display()
 #→ print:
#Name
#Marks
#School name
#👉 Outside the class:
#Create object
#Call set_details()
#Call display()
class student:
    school_name="XYZ School"
    def set_details(self):
        self.name="vamsi"
        self.marks=85
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
        print("School:",student.school_name)
o=student()
o.set_details()
o.display()

