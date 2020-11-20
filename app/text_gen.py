# create a file with the name random.txt of with 100 random characters
import random 
import string 
import os 
import os.path
from os import path

def findingFiles(): #function that finds files
    fileExistence = print("File exists:"+str(path.exists("random.txt"))) #prints a boolean if the file exists 
    if fileExistence == True: #if the file exists 
        file = open("random.txt", "w") #open the file 
        #print out existing content
        print (file.read())
    else:
        print("No such file exists")
        
def randomCharacters(length):
    text = " " #start off with an empty string 
    fileName = open("random.txt", "w")
    for i in range(length):
        text += random.choice(string.ascii_letters + string.digits + string.hexdigits)#adding ascii and string sto make up the characters for the text 
    fileName.write(text)
    fileName.close()
    #open the file 
    fileOpen = open("random.txt")
    

findingFiles()
randomCharacters(100)
findingFiles()
randomCharacters(100)

