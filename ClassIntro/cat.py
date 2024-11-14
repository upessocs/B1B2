from animal import Animal

class Cat(Animal):
    species = "Cat species"
    
    def meu(self):
        return f"{self.name} says meu!"