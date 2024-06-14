
class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        super().__init__()  # call the __init__ method of the parent class
        self.y = 1

def main():
    b = Derived_Test()
    print(b.x, b.y)

main()