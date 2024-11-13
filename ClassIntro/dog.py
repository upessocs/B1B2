from animal import Animal

class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"