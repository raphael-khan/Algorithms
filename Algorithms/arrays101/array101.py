
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

# person1 = Person('raphael', 33)
# print(person1.age)
# person1.age = 40
# print(person1.age)
# del person1.age
# print(person1.age)

int = [5]*3
# print(int)

int2 = [None]*3
# print(int2[1])

a = [5 for i in range(10)]
# print(a)

b = ['Hi' for i in range(5)]

# print(len(b))

randomArr = ['oranges', 'bananas', 5, False]
# for i in randomArr:
#     print(i)
#     if i == 5:
#         break

# for i in 'raphael':
#     print(i)

# for i in range(2,13,2):
#     print(i)
# else:
#     print('Finished')

adj = ['red', 'blue', 'white']
fruits = ['melon', 'banana', 'grapes']

# for i in adj:
#     for x in fruits:
#         print(i,x)
# i = 1
# while i < 10:
#     print(i)
#     if i == 7:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else: 
#     print('i is now 6 and the loop stops')