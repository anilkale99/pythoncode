'''
Created on Jul 25, 2018

@author: Anil.Kale
'''

#Set is a collection which is unordered and unindexed. No duplicate members.

carset = {"Rolls", "Jaguar", "Range Rover"}
print(carset)

for x in carset:
    print (x)
    
   
    

#this is set constructor with two barces, now you can add and remove element
fruitSet = set(("apple", "banana", "cherry")) # note the double round-brackets
fruitSet.add("Mango")
print(fruitSet)

#remove item
fruitSet.remove("banana")
print(fruitSet)


fruitSet.add("Orange")
print(fruitSet)

# Code will compile if you try to add duplicate element however there will not be any entry
fruitSet.add("Orange")
print(fruitSet) 

