class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__age = age# private
    
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    
    def __str__(self):
        return f"\nname is {self.name}\nage is {self.__age}\n"