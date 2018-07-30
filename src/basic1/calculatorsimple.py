'''
Created on Jul 23, 2018

@author: Anil.Kale
'''

print ("1. Add ")
print ("2. Subtract")


def myAddiction(x, y):
    return x+y 

def mySubstraction(x, y):
    return x - y 

choice = int(input("Enter option:  "))

if choice == 1:
    print ("addition is =", myAddiction(2, 4))

if choice == 2:
    print ("addition is =", mySubstraction(8, 4))
    