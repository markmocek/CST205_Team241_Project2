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


def openfile():
    filename = askopenfilename()
    file_opt = options = {}
    options['filetypes'] = [('all files', '.*'), ('wav files', '.wav')]
    f.open(filename)
    f.read()
    print tkFileDialog.askopenfilename()

#Function that shifts characters in 'message' based on a give number 'shift'
def crypt(msg,shift):
        #Set string to lower case
        message = msg.lower()
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
    #Create StringLength variable for later use
        strLength = 0
#path = 'Test.txt'


#Remove file
        os.remove(file)


#Collect length of the string
        strLength = len(msg)
#Place encrypted message in code variable
        code1 = encrypt(msg)

#Write encrypted message to file
        if len(code1) > 0:
           fe = open(filename, 'w')
           fe.write(code1)
           fe.close()

#Hide data in wav file	
        hide_data(filename, msg, "Hidden.wav", 1)


#Recover data from wav file
        recover_data(filename, "Recovered.txt", 1, strLength)

#Collect string to encrypt
        f = open("Recovered.txt", 'r')
        msg = f.read()
        f.close()

#Remove file
        os.remove("Recovered.txt")

#Place decrypted message in code variable
        code2 = decrypt(msg)
#Write encrypted message to file
        if len(code2) > 0:
           fe = open("DeCrypted.txt", 'w')
           fe.write(code2)
           fe.close()
           print ("Done")


def displayText():
    """ Display the Entry text value. """
    global entryWidget


    if entryWidget.get().strip() == "":
         tkMessageBox.showerror("Tkinter Entry Widget", "Enter Secret Message")
    else:
         tkMessageBox.showinfo("Tkinter Entry Widget", "Secret Message =" + entryWidget.get().strip())
         f = open("Message.txt","w")
         f.write(entryWidget.get().strip()) 
         f.close()
         file = open("Message.txt","r")
         msg = file
         print file.read()

if __name__ == "__main__":     
   
    root = Tk()
 

a = Button(root, text="Open", command= openfile)
a.pack()

root.title("Tkinter Entry Widget")
root["padx"] = 40
root["pady"] = 20   
     # Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root) 
     #Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Enter the text:"
entryLabel.pack(side=LEFT)

     # Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()

button = Button(root, text="Submit", command=displayText)
button.pack()

crypt = Button(root, text = "Encrypt", command = crypt)
crypt.pack()
root.geometry("300x200")
root.mainloop()
