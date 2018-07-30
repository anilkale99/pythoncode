'''
Created on Jul 26, 2018

@author: Anil.Kale
'''


class Person:
    
    mobile = 12345
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
        
p1 = Person("Jerry", 20)

print(p1.name)
print(p1.age)
print(p1.mobile)

print("Mobile is a {}".format(p1.mobile))


