import Tkinter
from Tkinter import *
import tkMessageBox
import tkFileDialog
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
import Tkconstants

   
print tkFileDialog.askopenfilename()

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
