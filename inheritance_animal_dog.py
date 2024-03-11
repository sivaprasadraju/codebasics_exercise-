# call parent constuctor using super() from child class

class Animal:
    def __init__(self, habitate):
        self.habitate = habitate

    def print_habitate(self):
        print(self.habitate)

    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("kennel")

    def sound(self):
        print("Wooh Wooh")

dog = Dog()
dog.print_habitate()
dog.sound()

