'''
Created on Aug 1, 2018

@author: Anil.Kale
'''
from MyInheritance.MyCar import MyCarClass

class MyInheritanceTestClass(MyCarClass):
    '''
    classdocs
    '''
    if __name__ == '__main__':
        print(" in main11")
        obj = MyCarClass()   
        obj.carSpeed()   
        print(" end main22")

    
 
 

    print(" in main")
    obj = MyCarClass()    
    obj.carSpeed()
    print(" end main")