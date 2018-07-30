'''
Created on Jul 25, 2018

@author: Anil.Kale
'''
from nt import remove

indaDict =    {
  "Maharashtra": "Mumbai",
  "Karnataka": "Banglore",
  "Goa": "Panaji"
}
print(indaDict)


#Add key value pair
indaDict["Gujrat"] = "Ahemedabad"
print (indaDict) 

#get value by Key
cap1 = indaDict.get("Goa")
print(cap1)

# Length of dictionary
print("Length = ", len(indaDict))

#remove 
del(indaDict["Karnataka"])
print (indaDict) 














