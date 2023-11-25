#3.a) Write a program to create 'class' and 'objects' in python. Use 'constructors' and 'destructors'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} has been born! Age: {self.age}")

    def display_info(self):
        print(f"{self.name} is {self.age} years old.")

    def __del__(self):
        print(f"Goodbye, {self.name}!")

# Creating objects of the class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling methods of the objects
person1.display_info()
person2.display_info()

# Deleting objects explicitly
del person1
del person2
'''
In this example, when a Person object is created, the constructor (__init__) is called,
and a birth message is printed. The display_info method can be used to display information about the person.
When an object is explicitly deleted (using del), the destructor (__del__) is called, and a farewell message is printed.
'''