#This is python code to take analogy of with()
with open('C:/Users/Acer/Desktop/Python/test3.txt') as file:
    data = file.read()

with open('C:/Users/Acer/Desktop/Python/test3.txt', "w") as file:
    file.write("Hello world")
#======================================================================================

#Analogy for using split() function

with open('C:/Users/Acer/Desktop/Python/test2.txt', "r") as file:
    data = file.readlines()
    for line in data:
        #split each line sentence in to words
        word = line.split()
        print(word)
        
#======================================================================================
