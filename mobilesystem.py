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

