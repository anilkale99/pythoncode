'''
Created on Jul 19, 2018

@author: Anil.Kale
'''


def capital_case(x):
    return x.capitalize()

def test_capital_case3():
    assert capital_case('anil') == 'Anil'
    
def test_capital_case4():
    assert (True) == True