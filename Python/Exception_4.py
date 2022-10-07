import sys

#if value is exceeds 50, the output will be  ValueError

try:
    x = int(input('Enter the first number: '))
    if x > 50:
        raise ValueError(x)  # if value of X > 50, Value exception will be raised.

except:
    print(sys.exc_info()[0])
