class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"this is {self.name} and he/she is {self.age}")

    def fly(self):
        print(f"{self.name} cannot fly")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def description(self):
        print(f"This guy {self.name} is cute and he is {self.age} old. His breed is {self.breed}")

    def fly(self):
        print(f"{self.name} cannot fly")

dog = Dog(name="Simba", age=5, breed="Lab")
animal = Animal(name="Leo", age=2)

dog.description()
animal.description()

dog.fly()
animal.fly()