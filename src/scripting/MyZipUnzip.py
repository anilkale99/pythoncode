'''
Created on Jul 25, 2018

@author: Anil.Kale
'''

import zipfile

zip = zipfile.ZipFile('D:\pythonscript\HelloPython.zip')  
zip.extractall('D:\pythonscript\output')  

