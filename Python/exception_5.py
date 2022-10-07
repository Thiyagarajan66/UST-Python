import sys




x = -10
if x < 0:
    raise Exception ("No number below 0 is allowed") 



x = 'Hello python'
if not type(x) is int:
    raise TypeError("only integers are allowed")
