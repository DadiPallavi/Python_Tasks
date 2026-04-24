class Student:
    school_name = "XYZ School"   

    def set_details(self):
        self.name = "Vamsi"
        self.marks = 85

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School Name:", self.school_name)



s = Student()      
s.set_details()    
s.display()   

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



e = Employee()          
e.set_data()            
e.increase_salary()    
e.display()             


class Mobile:
    brand = "Apple"
    def set_details(self):
        self.model = "iPhone 14"
        self.price = 80000
    def discount(self):
        self.price = self.price - (self.price * 10 / 100)
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
m = Mobile()          
m.set_details()       
m.discount()          
m.show_details() 

