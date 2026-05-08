class User():
    name="Pallavi"
    location="hyd"
    def __init__(self):
        pass
    def login(self):
        print("name:--",self.name)
        print("location:-- ", self.location)


class Customer(User):
    order_item="car"
    def __init__(self):
        pass
    def deliver_order(self):
        print("order_item:", self.order_item)
        super().login()
o=Customer()
o.deliver_order()

class DeliverPartner(User):
    vehicel_type="4 wheeler"
    def __init__(self):
        pass
    def deliver_order(self):
        print("vehicel type:--", self.vehicel_type)
        super().login()
k=DeliverPartner()
k.deliver_order()



    