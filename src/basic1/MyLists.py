'''
Created on Jul 25, 2018

@author: Anil.Kale
'''

# List is a collection which is ordered and changeable. Allows duplicate members. 

thislist = ["Pune", "Mumbai", "Delhi", 100]
print(thislist)

#Update value from list 
thislist = ["Selenium", "Java", "Eclipse"]
thislist[1] = "Python"
print(thislist)

# For loop for list
for x in thislist:
    print(x)
    
#Remove value
thislist.remove("Eclipse")
for x in thislist:
    print (x)
    
#return index of the value    
k = thislist.index("Selenium")
print (k)

#Returns count of the specified element     
c = thislist.count("Python")    
print (c)

lngth  = thislist.__len__()
print ("length 1= ",  lngth)

print ("length 2= ",  len(thislist))


thislist.append("Jenkins")
print(thislist)    

thislist.remove("Selenium")
print(thislist) 
    
    
    
    
    
    
    
    
    
    
    