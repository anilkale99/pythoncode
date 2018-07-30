'''
Created on Jul 25, 2018

@author: Anil.Kale
'''
import os


#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content


f = open("D:\pythonscript\output\myfile.txt", "w")  

appendFile = open("D:\pythonscript\output\myfile.txt", "w")
appendFile.write("Lets write in the file ")

#"x" - Create - will create a file, returns an error if the file exist
#os.remove("D:\pythonscript\output\HelloPython.py")
f = open("D:\pythonscript\output\myfile2.txt", "x") 















