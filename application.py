#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
from Tkinter import Frame, Tk, BOTH, Menu, Label, Button, BOTTOM
import tkFileDialog, pitrain

class Application(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)  

        self.width = 600
        self.height = 350
        self.padding = 10

        self.imageLabel = Label()
         
        self.parent = parent  
        self.centerWindow()      
        self.initUI()

    def centerWindow(self):
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()
        
        x = (screenWidth - self.width)/2
        y = (screenHeight - self.height)/2
        self.parent.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        
    def initUI(self):
        self.parent.title("Equations!")
        self.pack(fill=BOTH, expand=1)

        uploadFile = Image.open('upload.png')
        uploadPic = ImageTk.PhotoImage(uploadFile)
        uploadLabel = Label(self, image=uploadPic)
        uploadLabel.image = uploadPic
        uploadLabel.grid(row=0)

        openButton = Button(self, text="Import Image", command=self.onOpen, width=20, compound=BOTTOM)
        openButton.grid(row=1)


    def onOpen(self):
        ftypes = [('Images', '*.png'), ('All files', '*')]
        dialog = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dialog.show()
        
        if filename != '':
            pic = self.readFile(filename)

    def readFile(self, filename):
        picFile = Image.open(filename)
        #if the file is too big for the screen
        if picFile.size[0] > (self.width - (self.padding*2)):
            picFile.thumbnail((590,300), Image.ANTIALIAS) #weird padding issues make this number not even
        picture = ImageTk.PhotoImage(picFile)
        label = Label(self, image=picture)
        label.image = picture
        self.imageLabel.grid_remove() #remove the previous image if there is one
        label.grid(row=0)
        self.imageLabel = label #set this image to the global image
         

def main():
    root = Tk()
    ex = Application(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  