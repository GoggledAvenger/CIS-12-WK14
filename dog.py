# Interactive Exercises from https://thartmanoftheredwoods.github.io/CIS-12/week_14py.html

from copy import copy, deepcopy

from size import Size

class Dog:
    """dog"""

    def __init__(self,name:str,breed:str,age:int,size:Size):
        self.name = name
        self.breed = breed
        self.age = age
        self.size = size

    def __str__(self):
        return f'{self.name} is a {self.breed}, {self.age} years old, of {self.size} size.'

    def __eq__(self,other):
        return self.breed == other.breed and self.age == other.age and self.size == other.size

#testing

dog1 = Dog('Fido','pug', 6,Size('medium'))
dog2 = Dog('Fifi', 'pomeranian', 3,Size('small'))
dog3 = Dog('Rover','german shephard',10,Size('large'))
dog4 = copy(dog2)
dog5 = deepcopy(dog1)

dog4.size = Size('medium')
dog5.size = Size('small')

print(dog1)
print(dog2)
print(dog3)
print(dog4)
print(dog5)
#print(dog1 == dog2)
#print(dog1 is dog3)

