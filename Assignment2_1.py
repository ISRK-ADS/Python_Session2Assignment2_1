# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:33:51 2018

@author: krishna.i
 
Assignment 2.1: Write a program which accepts a sequence of comma-separated
numbers from console and generate a list.

"""

astring = str(input("ENTER Comma separated values: "))
print("String value is: ", astring) # printing of string value as given
alist = astring.split(sep=",")   # converting string value to list values and assigning to list variable
print("List Generated is: ", alist)  # printing list value generated

# End of the code