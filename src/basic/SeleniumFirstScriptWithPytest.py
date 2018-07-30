'''
Created on Jul 18, 2018

@author: Anil.Kale
'''
class MyClass(object):

        def capital_case(x):
            return x.capitalize()
        
        def test_capital_case1():
            assert capital_case('anil') == 'Anil'
            
        def test_capital_case2():
            assert (True) == True
    
def __init__(self, params):