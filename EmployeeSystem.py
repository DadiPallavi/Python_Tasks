class Employee :
    company = "Infosys"
    def set_data(self):
        self.name="Ravi"
        self.salary=20000
    def increase_salary(self):
        self.salary=self.salary+5000
    def display(self):
        print("Company ",Employee.company)
        print("Name: ", self.name)
        print("salary: ", self.salary)

k=Employee()
k.set_data()
k.increase_salary()
k.display()


