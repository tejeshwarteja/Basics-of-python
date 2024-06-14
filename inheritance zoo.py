class Animal:
    def __init__(self,name,species,sound):
        self.name = name
        self.species = species
        self.sound = sound
    def make_sound(self):
        print(f"the {self.species} named {self.name} says {self.sound}")

class Lion(Animal):
    def __init__(self,name):
        super().__init__(name,"Lion","roar")
    def display(self):
        print("lions are the kings of the jungle")

class Elephant(Animal):
    def __init__(self,name):
        super().__init__(name,"Elephant","trumpet")
    def display(self):
        print("Elephants are the largest land animals")

class Snake(Animal):
    def __init__(self,name):
        super().__init__(name,"Snake","hiss")
    def display(self):
        print("Snakes can be found on every continent")

l1= Lion("Leo")
e1= Elephant("Ellie")
s1= Snake("Slyther")

l1.make_sound()
l1.display()
e1.make_sound()
e1.display()
s1.make_sound()
s1.display()