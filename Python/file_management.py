"""
#Open file in read or text  mode, default mode

fileobj = open("path of the file")

#open file in the read mode
fileobj = open("path of the file", 'r')

#open file in the write mode
fileobj = open("path of the file", 'w')

#open file in the append mode
fileobj = open("path of the file", 'a')
--------------------------------------------"""

fileobj = open("C:/Users/Acer/Desktop/Python/test.txt")

#open file in the read mode
fileobj = open("C:/Users/Acer/Desktop/Python/test.txt", 'r')

#open file in the write mode
fileobj = open("C:/Users/Acer/Desktop/Python/test.txt", 'w')

#open file in the append mode
fileobj = open("C:/Users/Acer/Desktop/Python/test.txt", 'a')

#close the file
fileobj.close()

#read file
fileobj = open('C:/Users/Acer/Desktop/Python/test1.txt')
#read whole file
print(fileobj.read())

#bring the cursor in to the initial position
fileobj.seek(0)
print(fileobj.read())

#place the cursor at 7th position
fileobj.seek(7)
print(fileobj.read())

fileobj.seek(0)
#read frst 22 chars
print(fileobj.read(22))


#Find out the cursor position
print(fileobj.tell())

#readline()- reads the line of the file
print(fileobj.readline()) #reads the frst line

print(fileobj.readline()) #Reads the sec line 

print(fileobj.readline()) #reads the third line

#readlines()- read lines is use to read all the line of the file
fileobj.seek(0)
print(fileobj.readlines())

#reading frst 5 lines of the passsage
fileobj.seek(0)
count = 0
for i in fileobj.readlines():
    if (count < 5):
        print(i)

    else:
        break
    count+= 1

#===========================================================================

    #write mode
#write a file
fileobj2 = open('C:/Users/Acer/Desktop/Python/test2.txt','w')

#Add the content to existing file
fileobj2.write('The new content added to be in the newly created file by using write mode')
fileobj2.close()

fileobj2 = open('C:/Users/Acer/Desktop/Python/test2.txt','r')
print(fileobj2.read())
fileobj2.close()    #Must to close the file after read, else when deleting it will throw the error 'file is using by other...'


#===========================================================================

#delete a file
import os
os.remove("C:/Users/Acer/Desktop/Python/test2.txt") #once the file deleted we cant able to read thst file again

fileobj2 = open('C:/Users/Acer/Desktop/Python/test2.txt','r') #we will get 'file not found' after try to read the file after deletion

#============================================================================





    




























