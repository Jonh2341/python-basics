class Animal():
    def speak(self):
        print('some sound')
    
class Dog(Animal):
    def speak(self):
        print('woof!')

class Cat(Animal):
    def speak(self):
        print('mew!')

pets = [Dog(), Cat()]

for pet in pets:
    pet.speak()
    # polymorphism