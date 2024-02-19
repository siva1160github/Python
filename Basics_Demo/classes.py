class Person:
    def __init__(self, name, age, designation):
        self.Name = name
        self.Age = age
        self.Designation = designation

    def getAge(self):
        return self.Age
    
person1 = Person('siva', 28, 'FSD')
print(person1.getAge())