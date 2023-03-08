import os

import cv2
import mediapipe as mp
import numpy as np

mp_selfie_segmentation= mp.solutions.selfie_segmentation #call the function to use

photo_path= os.path.join('.','data','photo.jpg')
#photo_out_path= os.path.join('.','output.jpg') #Using the choose color
#bg_path= os.path.join('.','data','background.jfif')
#photo_out_path= os.path.join('.','outputBg.jpg') #Background 1
bg_path= os.path.join('.','data','background2.jfif')
photo_out_path= os.path.join('.','outputBg2.jpg') #Background 2

BG_COLOR= (78,43,22) #Navy blue

#Configuration options (model selections 0 or 1)
with mp_selfie_segmentation.SelfieSegmentation(
    model_selection=0) as selfie_segmentation:

    photo= cv2.imread(photo_path) #Pass the element to work

    #Change the original format BGR to RGB
    photo_rgb= cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)

    #Applicant selfie segmentation
    result= selfie_segmentation.process(photo_rgb) #With this result we change the background

    #Simple thresholding (umbralizacion simple) to improve the mask
    _, th= cv2.threshold(result.segmentation_mask,0.75,255, cv2.THRESH_BINARY) #All 0.75 became 255 or white obtein a binary image
    #print(th.dtype) #Result float32
    th= th.astype(np.uint8) #Format with working opencv
    th= cv2.medianBlur(th,13) #apply a filter to soften the edges

    #Inverting the binary image to manage the background and after sum to the profile
    th_inv= cv2.bitwise_not(th)

    #Background
    """ bg_img= np.ones(photo.shape, dtype=np.uint8) #Build an image with the color selected
    bg_img[:]= BG_COLOR """
    bg_img= cv2.imread(bg_path)
    bg_img= cv2.resize(bg_img,(photo.shape[1],photo.shape[0]), interpolation= cv2.INTER_CUBIC)
    bg_img= cv2.GaussianBlur(bg_img, (15,15),0)
    #print(bg_img.shape)
    #print(photo.shape)
    bg= cv2.bitwise_and(bg_img,bg_img, mask=th_inv)

    #Foreground
    fg= cv2.bitwise_and(photo,photo, mask= th)

    # Background + Foreground
    output_photo= cv2.add(bg, fg)

    #Save the image
    cv2.imwrite(photo_out_path, output_photo)

    cv2.imshow("Photo", photo)
    #cv2.imshow("Result mediapipe", result.segmentation_mask)
    #cv2.imshow("Th", th)
    #cv2.imshow("Invested Th", th_inv)
    cv2.imshow("Background", bg)
    cv2.imshow("Foreground", fg)
    cv2.imshow("Output photo", output_photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#If we work a video
""" cap= cv2.VideoCapture(0,photo_path) #Pass the element to work

#Configuration options (model selections 0 or 1)
with mp_selfie_segmentation.SelfieSegmentation(
    model_selection=0) as selfie_segmentation:

    while True:
        ret, frame= cap.read() #Pass the element to work
        if ret == False:
            break
        cv2.imshow("F", Frame)
        if cv2.waitKey(1) & 0xFF ==27:
            break
cap.release() """