"""
Arithmetic error----------- (when the calculations fails)
Zero divisoon error-------- (100/0 we can get the zero division errror)
EOF error ----------------- (if the brackets not closed properly, Inverted comas arent closed)
Index error---------------- (When an index is not found in a sequence)
Key error ----------------- (Key value, part of the dictionary)
File not found error------- (When the file is not present in the location)
Indentation error---------- (Happens when when indent is not specify properly)
Syntax error--------------- (Happens when the syntax are not declared properly)
ValueError----------------- (Occurs when built in function for a data type has the valid type of arguments have invalid values)
Assertion error------------ (When numberical calculations fails)
Overflow Errors------------ (Occurs when result of arithmetic operation is too large and  become machine unreadable)
Type Error----------------- (Happens when the incorrect type of function or operation is applied to an object)

"""
#When the exception occurs python interpreters stops the current process and passes it to the calling process untill its handled.
#if it is not handled the program will be crash.
#Exceptions in python can be handled using try statement, the TRY block lets you test the block of code for errors.
#The block of code which can raise an exception is placed inside the try clause.
#The code that will handle the exceptions is written in the except clause.
#the Finally code block will execute regardless of the result of the try and except block.
#We can also use the ELSE keyword to define the block of code to be executed if no exceptions were raised.

"""
TRY
TRY BLOCK
ELSE
EXCEPT
-------------
try:
    print(100/0) #Run block of code
except:
    print(sys.exc_info()[1],"Exception occured") #run this bloc of code when exception occurs

else:
    print("No exception occured")  #Run this code when no exception occurs

finally:
    print("run this block of code always")   #Run this code when no exception occurs  """
#============================================================================================================================
import sys

try:
    print(100//2)  #Zero division error will be executed here
    
except:
    print(sys.exc_info()[1],'Exception occured') #This statement will be executed only if exception occurs

else:
    print('No exception occured')

finally:
    print('Run this block of code always')#This statement will executed always
#============================================================================================================================
    


    


    
    
    
