#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import numpy as np
from PIL import Image, ImageTk
from Tkinter import Frame, Tk, BOTH, Menu, Label, Button, BOTTOM, TOP, NORMAL, S
import tkFileDialog, os
import cv2

global waitingForKey, trainingValue

class Application(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)  

        self.width = 600
        self.height = 350
        self.padding = 0

        self.imageLabel = Label()
        self.waitingForKey = True
         
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
        self.uploadLabel = Label(self, image=uploadPic)
        self.uploadLabel.image = uploadPic
        self.uploadLabel.grid(row=0)

        self.openButton = Button(self, text="Import Image", command=self.onOpen, width=20, compound=BOTTOM)
        self.openButton.grid(row=1)


    def onOpen(self):
        self.uploadLabel.grid_remove()
        self.openButton.grid_remove()
        ftypes = [('Images', '*.png'), ('All files', '*')]
        dialog = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dialog.show()
        
        if filename != '':
            trainFileName = self.readFile(filename)
            self.train(filename)
            #print("python pitrain.py " + filename)
            #os.system("python pitrain.py " + filename)


    def readFile(self, filename):
        picFile = Image.open(filename)
        #if the file is too big for the screen
        if picFile.size[0] > (self.width - (self.padding*2)):
            picFile.thumbnail((590,300), Image.ANTIALIAS) #weird padding issues make this number not even
        #picture = ImageTk.PhotoImage(picFile)
        #label = Label(self, image=picture)
        #label.image = picture
        #self.imageLabel.grid_remove() #remove the previous image if there is one
        #label.grid(row=0)
        #self.imageLabel = label #set this image to the global image

    def train(self, imageFile):
        global waitingForKey, trainingValue
        waitingForKey = True
        trainingValue = 99

        im = cv2.imread(imageFile)

        grayScale = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        #blur = cv2.GaussianBlur(grayScale,(5,5),0)
        thresh = cv2.adaptiveThreshold(grayScale,255,1,1,11,2)

        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

        samples =  np.empty((0,100))
        responses = []

        self.columnconfigure(0, minsize=390)
        self.rowconfigure(0, minsize=125)

        buttonImg_1 = ImageTk.PhotoImage(file="button_one.png")
        buttonImg_1_dwn = ImageTk.PhotoImage(file="button_one_dwn.png")
        self.button_1 = Label(self, image=buttonImg_1, cursor="pointinghand")
        self.button_1.image = buttonImg_1
        self.button_1.bind("<ButtonRelease-1>", lambda event: self.button_1.configure(image=buttonImg_1))
        self.button_1.grid(row=0, column=1, sticky=S)

        buttonImg_2 = ImageTk.PhotoImage(file="button_two.png")
        buttonImg_2_dwn = ImageTk.PhotoImage(file="button_two_dwn.png")
        self.button_2 = Label(self, image=buttonImg_2, cursor="pointinghand")
        self.button_2.image = buttonImg_2
        self.button_2.bind("<ButtonRelease-1>", lambda event: self.button_2.configure(image=buttonImg_2))
        self.button_2.grid(row=0, column=2, sticky=S)

        buttonImg_3 = ImageTk.PhotoImage(file="button_three.png")
        buttonImg_3_dwn = ImageTk.PhotoImage(file="button_three_dwn.png")
        self.button_3 = Label(self, image=buttonImg_3, cursor="pointinghand")
        self.button_3.image = buttonImg_3
        self.button_3.bind("<ButtonRelease-1>", lambda event: self.button_3.configure(image=buttonImg_3))
        self.button_3.grid(row=0, column=3, sticky=S)

        buttonImg_divide = ImageTk.PhotoImage(file="button_divide.png")
        buttonImg_divide_dwn = ImageTk.PhotoImage(file="button_divide_dwn.png")
        self.button_divide = Label(self, image=buttonImg_divide, cursor="pointinghand")
        self.button_divide.image = buttonImg_divide
        self.button_divide.bind("<ButtonRelease-1>", lambda event: self.button_divide.configure(image=buttonImg_divide))
        self.button_divide.grid(row=0, column=4, sticky=S)

        buttonImg_4 = ImageTk.PhotoImage(file="button_four.png")
        buttonImg_4_dwn = ImageTk.PhotoImage(file="button_four_dwn.png")
        self.button_4 = Label(self, image=buttonImg_4, cursor="pointinghand")
        self.button_4.image = buttonImg_4
        self.button_4.bind("<ButtonRelease-1>", lambda event: self.button_4.configure(image=buttonImg_4))
        self.button_4.grid(row=1, column=1)

        buttonImg_5 = ImageTk.PhotoImage(file="button_five.png")
        buttonImg_5_dwn = ImageTk.PhotoImage(file="button_five_dwn.png")
        self.button_5 = Label(self, image=buttonImg_5, cursor="pointinghand")
        self.button_5.image = buttonImg_5
        self.button_5.bind("<ButtonRelease-1>", lambda event: self.button_5.configure(image=buttonImg_5))
        self.button_5.grid(row=1, column=2)

        buttonImg_6 = ImageTk.PhotoImage(file="button_six.png")
        buttonImg_6_dwn = ImageTk.PhotoImage(file="button_six_dwn.png")
        self.button_6 = Label(self, image=buttonImg_6, cursor="pointinghand")
        self.button_6.image = buttonImg_6
        self.button_6.bind("<ButtonRelease-1>", lambda event: self.button_6.configure(image=buttonImg_6))
        self.button_6.grid(row=1, column=3)

        buttonImg_multiply = ImageTk.PhotoImage(file="button_multiply.png")
        buttonImg_multiply_dwn = ImageTk.PhotoImage(file="button_multiply_dwn.png")
        self.button_multiply = Label(self, image=buttonImg_multiply, cursor="pointinghand")
        self.button_multiply.image = buttonImg_multiply
        self.button_multiply.bind("<ButtonRelease-1>", lambda event: self.button_multiply.configure(image=buttonImg_multiply))
        self.button_multiply.grid(row=1, column=4)

        buttonImg_7 = ImageTk.PhotoImage(file="button_seven.png")
        buttonImg_7_dwn = ImageTk.PhotoImage(file="button_seven_dwn.png")
        self.button_7 = Label(self, image=buttonImg_7, cursor="pointinghand")
        self.button_7.image = buttonImg_7
        self.button_7.bind("<ButtonRelease-1>", lambda event: self.button_7.configure(image=buttonImg_7))
        self.button_7.grid(row=2, column=1)

        buttonImg_8 = ImageTk.PhotoImage(file="button_eight.png")
        buttonImg_8_dwn = ImageTk.PhotoImage(file="button_eight_dwn.png")
        self.button_8 = Label(self, image=buttonImg_8, cursor="pointinghand")
        self.button_8.image = buttonImg_8
        self.button_8.bind("<ButtonRelease-1>", lambda event: self.button_8.configure(image=buttonImg_8))
        self.button_8.grid(row=2, column=2)

        buttonImg_9 = ImageTk.PhotoImage(file="button_nine.png")
        buttonImg_9_dwn = ImageTk.PhotoImage(file="button_nine_dwn.png")
        self.button_9 = Label(self, image=buttonImg_9, cursor="pointinghand")
        self.button_9.image = buttonImg_9
        self.button_9.bind("<ButtonRelease-1>", lambda event: self.button_9.configure(image=buttonImg_9))
        self.button_9.grid(row=2, column=3)

        buttonImg_subtract = ImageTk.PhotoImage(file="button_subtract.png")
        buttonImg_subtract_dwn = ImageTk.PhotoImage(file="button_subtract_dwn.png")
        self.button_subtract = Label(self, image=buttonImg_subtract, cursor="pointinghand")
        self.button_subtract.image = buttonImg_subtract
        self.button_subtract.bind("<ButtonRelease-1>", lambda event: self.button_subtract.configure(image=buttonImg_subtract))
        self.button_subtract.grid(row=2, column=4)

        buttonImg_0 = ImageTk.PhotoImage(file="button_zero.png")
        buttonImg_0_dwn = ImageTk.PhotoImage(file="button_zero_dwn.png")
        self.button_0 = Label(self, image=buttonImg_0, cursor="pointinghand")
        self.button_0.image = buttonImg_0
        self.button_0.bind("<ButtonRelease-1>", lambda event: self.button_0.configure(image=buttonImg_0))
        self.button_0.grid(row=3, column=2)

        buttonImg_add = ImageTk.PhotoImage(file="button_add.png")
        buttonImg_add_dwn = ImageTk.PhotoImage(file="button_add_dwn.png")
        self.button_add = Label(self, image=buttonImg_add, cursor="pointinghand")
        self.button_add.image = buttonImg_add
        self.button_add.bind("<ButtonRelease-1>", lambda event: self.button_add.configure(image=buttonImg_add))
        self.button_add.grid(row=3, column=4)

        for cnt in contours:
            if cv2.contourArea(cnt)>50:
                [x,y,w,h] = cv2.boundingRect(cnt)
                if  h>40:
                    #cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),0)
                    roi = thresh[y:y+h,x:x+w]
                    roismall = cv2.resize(roi,(10,10))
                    crop = im[y:y+h, x:x+w]
                    constant= cv2.copyMakeBorder(crop,100,100,100,100,cv2.BORDER_CONSTANT,value=(255,255,255))
                    #cv2.imshow('norm',constant)
                    a = Image.fromarray(constant)
                    #a = Image.open(imageFile)
                    #b = ImageTk.PhotoImage(image=a)
                    #app.imageLabel.configure(image=b)
                    #app.update()

                    picture = ImageTk.PhotoImage(a)
                    label = Label(self, image=picture)
                    label.image = picture
                    self.imageLabel.grid_remove() #remove the previous image if there is one
                    label.grid(row=0, column=0, rowspan=4)
                    self.imageLabel = label #set this image to the global image



                    while(waitingForKey):
                        self.button_1.bind("<Button-1>", lambda event: callback(event, 1, self.button_1, buttonImg_1_dwn))
                        self.button_2.bind("<Button-1>", lambda event: callback(event, 2, self.button_2, buttonImg_2_dwn))
                        self.button_3.bind("<Button-1>", lambda event: callback(event, 3, self.button_3, buttonImg_3_dwn))
                        self.button_4.bind("<Button-1>", lambda event: callback(event, 4, self.button_4, buttonImg_4_dwn))
                        self.button_5.bind("<Button-1>", lambda event: callback(event, 5, self.button_5, buttonImg_5_dwn))
                        self.button_6.bind("<Button-1>", lambda event: callback(event, 6, self.button_6, buttonImg_6_dwn))
                        self.button_7.bind("<Button-1>", lambda event: callback(event, 7, self.button_7, buttonImg_7_dwn))
                        self.button_8.bind("<Button-1>", lambda event: callback(event, 8, self.button_8, buttonImg_8_dwn))
                        self.button_9.bind("<Button-1>", lambda event: callback(event, 9, self.button_9, buttonImg_9_dwn))
                        self.button_0.bind("<Button-1>", lambda event: callback(event, 0, self.button_0, buttonImg_0_dwn))
                        self.button_divide.bind("<Button-1>", lambda event: callback(event, 11, self.button_divide, buttonImg_divide_dwn))
                        self.button_multiply.bind("<Button-1>", lambda event: callback(event, 12, self.button_multiply, buttonImg_multiply_dwn))
                        self.button_subtract.bind("<Button-1>", lambda event: callback(event, 13, self.button_subtract, buttonImg_subtract_dwn))
                        self.button_add.bind("<Button-1>", lambda event: callback(event, 14, self.button_add, buttonImg_add_dwn))
                        self.update()

                    #key = cv2.waitKey(0)

                    #if key == 27:  # (escape to quit)
                    #    sys.exit()
                    #elif key in keys:
                    #    responses.append((chr(key)))
                    #    sample = roismall.reshape((1,100))
                    #    samples = np.append(samples,sample,0)
                    responses.append(trainingValue)
                    sample = roismall.reshape((1,100))
                    samples = np.append(samples,sample,0)
                    waitingForKey = True

        responses = np.array(responses,np.float32)
        responses = responses.reshape((responses.size,1))

        trainingCompFile = Image.open('trainingcompleted.png')
        trainingCompPic = ImageTk.PhotoImage(trainingCompFile)
        self.uploadLabel = Label(self, image=trainingCompPic)
        self.uploadLabel.image = trainingCompPic
        self.uploadLabel.grid(row=0)

        sampleData = file('generalsamples.data', 'a')
        np.savetxt(sampleData,samples)
        sampleData.close()

        responseData = file('generalresponses.data', 'a')
        np.savetxt(responseData,responses)
        responseData.close()
         

def main():
    root = Tk()
    ex = Application(root)
    root.mainloop()

def callback(event, value, label, labelImage):
        global waitingForKey, trainingValue

        label.configure(image=labelImage)

        trainingValue = value
        print value
        waitingForKey = False


if __name__ == '__main__':
    main()  