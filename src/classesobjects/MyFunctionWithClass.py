'''
Created on Jul 26, 2018

@author: Anil.Kale
'''


class MyFunctionClass:
    
    def testMethod1(self, i):
        print (" in method 1 ",i )

    def testMethod2(self):
        print (" in method 2")
    
    def testMethod3(self):
        print (" in method 3")
        
        
obj = MyFunctionClass()
obj.testMethod1(10)
obj.testMethod2()