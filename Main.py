'''
CST205 - Project 2 - Sean Vucinich, Abel , Mark Mocek - 3/16/17

Abel - Created the Graphic User Interface. Gathering text from user for the program to
encrypt and hide in wav file.

Sean - Created the WavSteg file that hides data inside a wav file. The program takes
text from a file and distributes bits across the wav file. The program also
goes back through the wav file and recovers those hidden bits, converts them back to
text, and places them in a text file.

Mark - Created the character encryption function. The function takes the text file
given and encrypts the text by shifting each character three positions in the alphabet.
The function also takes the text file from the hiding recovery and decrypts it from the
shift encrpytion by shifting it back three positions.
'''

import Tkinter
from Tkinter import *
import tkMessageBox
import tkFileDialog
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
import Tkconstants
from WavSteg import hide_data
from WavSteg import recover_data
from WavSteg import usage
import os

#Function that shifts characters in 'message' based on a give number 'shift'
def helper(message, shift):
    #Set string to lower case
	message = message.lower()
	#Set string to hold characters
	code = ""
	
	#Encrypt String
	for c in message:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			# wrap list if necessary
			if num > ord("z"):
				num -= 26
			elif num < ord("a"):
				num += 26
			code = code + chr(num)
		#Only modify letters
		else:
			code = code + c
	return code

#Encrypts the string and returns the result.
def encrypt(message):
	return helper(message, 3)

#Decrypts the string and returns the result.
def decrypt(message):
	return helper(message, -3)


#---------------GUI------------------
print tkFileDialog.askopenfilename()

def displayText():
    """ Display the Entry text value. """
    global entryWidget


    if entryWidget.get().strip() == "":
         tkMessageBox.showerror("Tkinter Entry Widget", "Enter Secret Message")
    else:
         tkMessageBox.showinfo("Tkinter Entry Widget", "Secret Message =" + entryWidget.get().strip())
         f = open("Message.txt","w")
         path = 'Message.txt'
         f.write(entryWidget.get().strip()) 
         f.close()

if __name__ == "__main__":     
   
    root = Tk()
 
root.title("Tkinter Entry Widget")
root["padx"] = 40
root["pady"] = 20   
     
textFrame = Frame(root) 
     
entryLabel = Label(textFrame)
entryLabel["text"] = "Enter the text:"
entryLabel.pack(side=LEFT)
  
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()

button = Button(root, text="Submit", command=displayText)
button.pack()

root.mainloop()
#--------------/GUI--------------------

#Create StringLength variable for later use
strLength = 0
#path = 'Test.txt'

#Collect string to encrypt
f = open(path, 'r')
msg = f.read()
f.close()

#Remove file
os.remove(path)


#Collect length of the string
strLength = len(msg)
#Place encrypted message in code variable
code = encrypt(msg)

#Write encrypted message to file
if len(code) > 0:
    fe = open(path, 'w')
    fe.write(code)
    fe.close()

#Hide data in wav file	
hide_data("Alice.wav", path, "Hidden.wav", 1)


#Recover data from wav file
recover_data("Alice.wav", "Recovered.txt", 1, 4)

#Collect string to encrypt
f = open("Recovered.txt", 'r')
msg = f.read()
f.close()

#Remove file
os.remove("Recovered.txt")

#Place decrypted message in code variable
code = decrypt(msg)
#Write encrypted message to file
if len(code) > 0:
    fe = open("DeCrypted.txt", 'w')
    fe.write(code)
    fe.close()


print ("Done")
