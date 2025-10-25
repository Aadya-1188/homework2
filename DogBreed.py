class Dog:
    animal = "Dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def display(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Color:", self.color)


dog1 = Dog("Labrador", "Golden")
dog2 = Dog("Beagle", "Brown and White")

dog1.display()
print()
dog2.display()
