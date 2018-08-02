'''
Created on Aug 2, 2018

@author: Anil.Kale
'''

class MyShape(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
     
    def area(self):
        print("shape : printing area")
        

class MySquare(MyShape):
    
    #def area(self):
    #    print("square : printing area")
     
    def sides(self):
        print("square : printing sides")
        


#Driver code        
obj = MySquare()
obj.area()    











