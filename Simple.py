class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""

    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

car1 = Car()
car1.brand = "Toyota"
car1.model = "Corolla"
car1.display()
