class car :
    def __init__ (self,model,price):
        self.model = model
        self.price = price

    def show_model(self):
        print(self.model)

    def update_model(self,new_model):
        self.model = new_model

car1 = car("r8",10000)

print(car1.model)

car1.show_model()

car2 = car("r15",50000)


