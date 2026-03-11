## Single Inheritance
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed

    def __str__(self):
        return f'{self.name} {self.breed}'

    def speak(self):
        print(f'{self.name} {self.breed} speaks Woof')

dog1=Dog('Tommy','dog','german')

print(dog1)

dog1.speak()
