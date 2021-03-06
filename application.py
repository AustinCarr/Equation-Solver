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

        uploadFile = Image.open('resources/upload.png')
        uploadPic = ImageTk.PhotoImage(uploadFile)
        self.uploadLabel = Label(self, image=uploadPic)
        self.uploadLabel.image = uploadPic
        self.uploadLabel.grid(row=0, columnspan=2)
        self.columnconfigure(0, minsize=100)

        self.trainButton = Button(self, text="Train", command=self.openTrain, width=20, compound=BOTTOM)
        self.trainButton.grid(row=1)

        self.solveButton = Button(self, text="Solve", command=self.openSolve, width=20, compound=BOTTOM)
        self.solveButton.grid(row=1,column=1)

    def openTrain(self):
        self.uploadLabel.grid_remove()
        self.trainButton.grid_remove()
        self.solveButton.grid_remove()
        ftypes = [('Images', '*.png'), ('All files', '*')]
        dialog = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dialog.show()

        if filename != '':
            self.train(filename)

    def openSolve(self):
        self.uploadLabel.grid_remove()
        self.trainButton.grid_remove()
        self.solveButton.grid_remove()
        ftypes = [('Images', '*.png'), ('All files', '*')]
        dialog = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dialog.show()
        
        if filename != '':
            self.solve(filename)

    def train(self, imageFile):
        global waitingForKey, trainingValue
        waitingForKey = True
        trainingValue = 99

        im = cv2.imread(imageFile)

        grayScale = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(grayScale,255,1,1,11,2)

        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

        samples =  np.empty((0,100))
        responses = []

        self.columnconfigure(0, minsize=390)
        self.rowconfigure(0, minsize=125)

        buttonImg_1 = ImageTk.PhotoImage(file="resources/button_one.png")
        buttonImg_1_dwn = ImageTk.PhotoImage(file="resources/button_one_dwn.png")
        self.button_1 = Label(self, image=buttonImg_1, cursor="pointinghand")
        self.button_1.image = buttonImg_1
        self.button_1.bind("<ButtonRelease-1>", lambda event: self.button_1.configure(image=buttonImg_1))
        self.button_1.grid(row=0, column=1, sticky=S)

        buttonImg_2 = ImageTk.PhotoImage(file="resources/button_two.png")
        buttonImg_2_dwn = ImageTk.PhotoImage(file="resources/button_two_dwn.png")
        self.button_2 = Label(self, image=buttonImg_2, cursor="pointinghand")
        self.button_2.image = buttonImg_2
        self.button_2.bind("<ButtonRelease-1>", lambda event: self.button_2.configure(image=buttonImg_2))
        self.button_2.grid(row=0, column=2, sticky=S)

        buttonImg_3 = ImageTk.PhotoImage(file="resources/button_three.png")
        buttonImg_3_dwn = ImageTk.PhotoImage(file="resources/button_three_dwn.png")
        self.button_3 = Label(self, image=buttonImg_3, cursor="pointinghand")
        self.button_3.image = buttonImg_3
        self.button_3.bind("<ButtonRelease-1>", lambda event: self.button_3.configure(image=buttonImg_3))
        self.button_3.grid(row=0, column=3, sticky=S)

        buttonImg_divide = ImageTk.PhotoImage(file="resources/button_divide.png")
        buttonImg_divide_dwn = ImageTk.PhotoImage(file="resources/button_divide_dwn.png")
        self.button_divide = Label(self, image=buttonImg_divide, cursor="pointinghand")
        self.button_divide.image = buttonImg_divide
        self.button_divide.bind("<ButtonRelease-1>", lambda event: self.button_divide.configure(image=buttonImg_divide))
        self.button_divide.grid(row=0, column=4, sticky=S)

        buttonImg_4 = ImageTk.PhotoImage(file="resources/button_four.png")
        buttonImg_4_dwn = ImageTk.PhotoImage(file="resources/button_four_dwn.png")
        self.button_4 = Label(self, image=buttonImg_4, cursor="pointinghand")
        self.button_4.image = buttonImg_4
        self.button_4.bind("<ButtonRelease-1>", lambda event: self.button_4.configure(image=buttonImg_4))
        self.button_4.grid(row=1, column=1)

        buttonImg_5 = ImageTk.PhotoImage(file="resources/button_five.png")
        buttonImg_5_dwn = ImageTk.PhotoImage(file="resources/button_five_dwn.png")
        self.button_5 = Label(self, image=buttonImg_5, cursor="pointinghand")
        self.button_5.image = buttonImg_5
        self.button_5.bind("<ButtonRelease-1>", lambda event: self.button_5.configure(image=buttonImg_5))
        self.button_5.grid(row=1, column=2)

        buttonImg_6 = ImageTk.PhotoImage(file="resources/button_six.png")
        buttonImg_6_dwn = ImageTk.PhotoImage(file="resources/button_six_dwn.png")
        self.button_6 = Label(self, image=buttonImg_6, cursor="pointinghand")
        self.button_6.image = buttonImg_6
        self.button_6.bind("<ButtonRelease-1>", lambda event: self.button_6.configure(image=buttonImg_6))
        self.button_6.grid(row=1, column=3)

        buttonImg_multiply = ImageTk.PhotoImage(file="resources/button_multiply.png")
        buttonImg_multiply_dwn = ImageTk.PhotoImage(file="resources/button_multiply_dwn.png")
        self.button_multiply = Label(self, image=buttonImg_multiply, cursor="pointinghand")
        self.button_multiply.image = buttonImg_multiply
        self.button_multiply.bind("<ButtonRelease-1>", lambda event: self.button_multiply.configure(image=buttonImg_multiply))
        self.button_multiply.grid(row=1, column=4)

        buttonImg_7 = ImageTk.PhotoImage(file="resources/button_seven.png")
        buttonImg_7_dwn = ImageTk.PhotoImage(file="resources/button_seven_dwn.png")
        self.button_7 = Label(self, image=buttonImg_7, cursor="pointinghand")
        self.button_7.image = buttonImg_7
        self.button_7.bind("<ButtonRelease-1>", lambda event: self.button_7.configure(image=buttonImg_7))
        self.button_7.grid(row=2, column=1)

        buttonImg_8 = ImageTk.PhotoImage(file="resources/button_eight.png")
        buttonImg_8_dwn = ImageTk.PhotoImage(file="resources/button_eight_dwn.png")
        self.button_8 = Label(self, image=buttonImg_8, cursor="pointinghand")
        self.button_8.image = buttonImg_8
        self.button_8.bind("<ButtonRelease-1>", lambda event: self.button_8.configure(image=buttonImg_8))
        self.button_8.grid(row=2, column=2)

        buttonImg_9 = ImageTk.PhotoImage(file="resources/button_nine.png")
        buttonImg_9_dwn = ImageTk.PhotoImage(file="resources/button_nine_dwn.png")
        self.button_9 = Label(self, image=buttonImg_9, cursor="pointinghand")
        self.button_9.image = buttonImg_9
        self.button_9.bind("<ButtonRelease-1>", lambda event: self.button_9.configure(image=buttonImg_9))
        self.button_9.grid(row=2, column=3)

        buttonImg_subtract = ImageTk.PhotoImage(file="resources/button_subtract.png")
        buttonImg_subtract_dwn = ImageTk.PhotoImage(file="resources/button_subtract_dwn.png")
        self.button_subtract = Label(self, image=buttonImg_subtract, cursor="pointinghand")
        self.button_subtract.image = buttonImg_subtract
        self.button_subtract.bind("<ButtonRelease-1>", lambda event: self.button_subtract.configure(image=buttonImg_subtract))
        self.button_subtract.grid(row=2, column=4)

        buttonImg_0 = ImageTk.PhotoImage(file="resources/button_zero.png")
        buttonImg_0_dwn = ImageTk.PhotoImage(file="resources/button_zero_dwn.png")
        self.button_0 = Label(self, image=buttonImg_0, cursor="pointinghand")
        self.button_0.image = buttonImg_0
        self.button_0.bind("<ButtonRelease-1>", lambda event: self.button_0.configure(image=buttonImg_0))
        self.button_0.grid(row=3, column=2)

        buttonImg_add = ImageTk.PhotoImage(file="resources/button_add.png")
        buttonImg_add_dwn = ImageTk.PhotoImage(file="resources/button_add_dwn.png")
        self.button_add = Label(self, image=buttonImg_add, cursor="pointinghand")
        self.button_add.image = buttonImg_add
        self.button_add.bind("<ButtonRelease-1>", lambda event: self.button_add.configure(image=buttonImg_add))
        self.button_add.grid(row=3, column=4)

        for contour in contours:
            if cv2.contourArea(contour)>50:
                [x,y,w,h] = cv2.boundingRect(contour)
                if  ((h>40) or (h > 28 and h < 33) or (h > 3 and h < 7)):
                    regionOfInterest = thresh[y:y+h,x:x+w]
                    regionOfInterestSmall = cv2.resize(regionOfInterest,(10,10))
                    crop = im[y:y+h, x:x+w]
                    constant= cv2.copyMakeBorder(crop,100,100,100,100,cv2.BORDER_CONSTANT,value=(255,255,255))
                    a = Image.fromarray(constant)

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

                    responses.append(trainingValue)
                    sample = regionOfInterestSmall.reshape((1,100))
                    samples = np.append(samples,sample,0)
                    waitingForKey = True

        responses = np.array(responses,np.float32)
        responses = responses.reshape((responses.size,1))

        trainingCompFile = Image.open('resources/trainingcompleted.png')
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

        self.button_1.grid_remove()
        self.button_2.grid_remove()
        self.button_3.grid_remove()
        self.button_4.grid_remove()
        self.button_5.grid_remove()
        self.button_6.grid_remove()
        self.button_7.grid_remove()
        self.button_8.grid_remove()
        self.button_9.grid_remove()
        self.button_0.grid_remove()
        self.button_add.grid_remove()
        self.button_subtract.grid_remove()
        self.button_multiply.grid_remove()
        self.button_divide.grid_remove()

    def displaySolution(self, solutionString):
        for x in range(len(solutionString)):
            solutionFile = Image.open("resources/" + solutionString[x:x+1] + ".png")
            solutionImage = ImageTk.PhotoImage(solutionFile)
            solutionLabel = Label(self, image=solutionImage)
            solutionLabel.image = solutionImage
            self.columnconfigure((6+x), minsize=10)
            solutionLabel.grid(row=0,column=(6+x))

    def solve(self, imageFile):
        samples = np.loadtxt('generalsamples.data',np.float32)
        responses = np.loadtxt('generalresponses.data',np.float32)
        responses = responses.reshape((responses.size,1))

        model = cv2.KNearest()
        model.train(samples,responses)
        im = cv2.imread(imageFile)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        xValues = {}

        out = np.zeros(im.shape,np.uint8)

        thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            index = 0
            if cv2.contourArea(contour)>50:
                [x,y,w,h] = cv2.boundingRect(contour)
                if  ((h>40) or (h > 28 and h < 33) or (h > 3 and h < 7)):
                    regionOfInterest = thresh[y:y+h,x:x+w]
                    regionOfInterestSmall = cv2.resize(regionOfInterest,(10,10))
                    regionOfInterestSmall = regionOfInterestSmall.reshape((1,100))
                    regionOfInterestSmall = np.float32(regionOfInterestSmall)
                    retval, results, neigh_resp, dists = model.find_nearest(regionOfInterestSmall, k = 1)
                    string = str(int((results[0][0])))
                    if(string == "14"):
                        string = "+"
                    if(string == "13"):
                        string = "-"
                    if(string == "12"):
                        string = "*"
                    if(string == "11"):
                        string = "/"

                    uploadFile = Image.open(imageFile)
                    picture = ImageTk.PhotoImage(uploadFile)
                    label = Label(self, image=picture)
                    label.image = picture
                    self.imageLabel.grid_remove() #remove the previous image if there is one
                    label.grid(row=0, column=0, columnspan=4)
                    self.imageLabel = label #set this image to the global image

                    equalsFile = Image.open("resources/equals.png")
                    equalsImage = ImageTk.PhotoImage(equalsFile)
                    equalsLabel = Label(self, image=equalsImage)
                    equalsLabel.image = equalsImage
                    equalsLabel.grid(row=0,column=5)

                    xValues[x] = string
                    index+=1

        xSortedList = sorted(xValues)
        equation = ""
        for item in xSortedList:
            equation += str(xValues[item])
        self.displaySolution((str)(eval(equation)))
        print(equation + "=" + (str)(eval(equation)))

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