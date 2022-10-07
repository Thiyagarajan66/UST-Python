

#Handling specific exception 



import os
import sys


try:
    x = int(input("enter the first number: "))
    y = int(input("enter the second number: "))
    print(x/y)
    os.remove('C:/Users/Acer/Desktop/Python/File_not_there.txt')
    
except NameError:
    print("Name error excpetion occured")

except FileNotFoundError:
    print("File not found excpetion occured")

except ZeroDivisionError:
    print("ZeroDivisionError occured")
    
    
