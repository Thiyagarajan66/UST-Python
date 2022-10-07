import sys
import os


try:
    os.remove('C:/Users/Acer/Desktop/Python/File_not_there.txt') #File not found error will occur as 'file_not_there/txt' is not in the location

except:
    print("Below exception occured")
    print(sys.exc_info()[1])

else:
    print('no exception occured')

finally:
    print('run this bloc of code always')
