
array = [True, 3, 'string']
# Let's put the DVD for The Avengers into the eighth place of the Array we created above.

#1 create dvd object. 

# blueprint 
class Dvd:
    name = 'Coolest movie ever'
    year = 2022

#an object out of that blue print 
actionMovie = Dvd()
# print(actionMovie.name)
# print(actionMovie.year)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello, my name is '+ self.name + ' and I am '+ str(self.age) + ' years old')

person1 = Person('raphael', 33)
print(person1.age)
person1.age = 40
print(person1.age)
del person1.age
print(person1.age)
