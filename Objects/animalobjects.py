# animalobjects.py
# practice object-oriented programming
# in the context of animals

class Animal():
    # constructor
    def __init__(self):
        self.name = "Unnamed"
        self.legs = 0

    # method
    def talk(self):
        if self.name != "Unnamed":
            print(f"Hello my name is, {self.name}!")
        else:
            print("Hello!")

# creating an animal object
some_animal = Animal()
# access properties
print(some_animal.name)
some_animal.name = "Rex"
some_animal.legs = 2
print(some_animal.name)

# TODO: Create a new object
#   * name it whatever you like
#   * give it 20 legs
#   * print out the name and legs

some_other_animal = Animal()
print(some_other_animal.name)
some_other_animal.name = "Xer"
some_other_animal.legs = 20
print(f"{some_other_animal.name}\n{some_other_animal}")
print(type(some_other_animal))
some_other_animal.talk()

another_animal = Animal()
another_animal.talk()







