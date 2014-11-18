import cv2
import numpy as np

#######   training part    ############### 
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.KNearest()
model.train(samples,responses)

############################# testing part  #########################

im = cv2.imread('helvtrain.png')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#im2 = cv2.imread('helv_match_5.png')
#gray2 = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

#ret,thresh2 = cv2.threshold(gray2,127,255,0)
#thresh2 = cv2.adaptiveThreshold(gray2,255,1,1,11,2)
#contours2, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


out = np.zeros(im.shape,np.uint8)

thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    index = 0
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>40:
            #cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
            string = str(int((results[0][0])))
            #ret = cv2.matchShapes(cnt,contours2[index],1,0.0)
            #if ret < 1.0:
            #    string = str(5)
            #cv2.drawContours(im, contours2[index], -1, (0,255,0), 3)
            cv2.drawContours(im, cnt, -1, (0,255,0), 3)
            cv2.putText(out,string,(x,y+h),0,1,(255,255,255))
            print(string)
            #print(ret)
            index+=1

cv2.imshow('im',im)
cv2.imshow('out',out)
cv2.waitKey(0)