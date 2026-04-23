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