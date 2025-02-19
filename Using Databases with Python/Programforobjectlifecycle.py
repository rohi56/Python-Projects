#Program for object life cycle
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")
    def __del__(self):
        print("Person destroyed")
    def display(self):
        print("Name:", self.name, ", Age:", self.age)
p1 = Person("John", 22)
p2 = Person("Paul", 23)
p1.display()
p2.display()
del p1
del p2
print("End of program")
