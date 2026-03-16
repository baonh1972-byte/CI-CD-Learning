# my_module.py
def greet(name):
    """Greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# main.py
import my_module

my_module.greet("Alice")  # Output: Hello, Alice!
result = my_module.add(5, 3)
print(result)  # Output: 8

def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

greet("Bob")  # Output: Hello, Bob!

class Dog:
    """A simple class representing a dog."""

    def __init__(self, name, breed):
        """Initializes the dog's name and breed."""
        self.name = name
        self.breed = breed

    def bark(self):
        """Simulates the dog barking."""
        print("Woof!")

# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
my_dog.bark()  # Output: Woof!