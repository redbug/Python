#!/usr/bin/python
'''
Created on Jul 20, 2011

@author: redbug
'''
import cv
import os
import sys
from optparse import OptionParser

class FaceFilter(object):
    '''
    This class is used for filter the photo which contains any person's face in it.
    '''
    #===========================================================================
    # haarcascade_profileface.xml
    # haarcascade_eye.xml
    # haarcascade_eye_tree_eyeglasses.xml
    # haarcascade_mcs_eyepair_big.xml
    # haarcascade_mcs_eyepair_small.xml
    # haarcascade_mcs_mouth.xml
    # haarcascade_mcs_nose.xml
    #===========================================================================
    CASCADE_DIR = '/usr/local/Cellar/opencv/2.2/share/opencv/haarcascades/'
    CASCADE_FACE_DEFAULT = CASCADE_DIR + 'haarcascade_frontalface_default.xml'
    CASCADE_FACE_ALT_1 = CASCADE_DIR + 'haarcascade_frontalface_alt.xml'
    CASCADE_FACE_ALT_2 = CASCADE_DIR + 'haarcascade_frontalface_alt2.xml'
    CASCADE_FACE_ALT_TREE = CASCADE_DIR + 'haarcascade_frontalface_alt_tree.xml'
    CASCADE_LOWERBODY = CASCADE_DIR + 'haarcascade_lowerbody.xml'
    CASCADE_UPPERBODY = CASCADE_DIR + 'haarcascade_mcs_upperbody.xml' 
    CASCADE_FULLBODY = CASCADE_DIR + 'haarcascade_fullbody.xml'
     
    #CASCADE_TUPLE = (CASCADE_LOWERBODY, CASCADE_FULLBODY, CASCADE_FACE_ALT_1, CASCADE_FACE_ALT_2, CASCADE_FACE_ALT_TREE)
    CASCADE_TUPLE = (CASCADE_FACE_ALT_1, CASCADE_FULLBODY)
    PHOTO_PATH = "/Users/redbug/Desktop/test_photos/"
    EXCLUDE_STRING = ("DS_Store", ".gif", "GIF")
    
    MIN_SIZE = (20, 20) #the smaller, the more accuracy, default=20,20
    IMAGE_SCALE = 2     #the smaller, the more accuracy, default=2
    HAAR_SCALE = 1.2    #the smaller, the more accuracy, default=1.2
    MIN_NEIGHBORS = 2   #the bigger, the more accuracy, default=2
    HAAR_FLAGS = 0    
    #HAAR_FLAGS = cv.CV_HAAR_DO_CANNY_PRUNING  # faster but less accuracy
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def dectect(self, img, file_name):
        gray = cv.CreateImage( (img.width,img.height), 8, 1 )
        small_img = cv.CreateImage((cv.Round(img.width / FaceFilter.IMAGE_SCALE),
                                    cv.Round (img.height / FaceFilter.IMAGE_SCALE)), 8, 1)
    
        # convert color input image to grayscale
        cv.CvtColor(img, gray, cv.CV_BGR2GRAY)
    
        # scale input image for faster processing
        cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)
    
        cv.EqualizeHist(small_img, small_img)
    
        dectected_objects=[]
        
        t = cv.GetTickCount()
        
        for cascade in FaceFilter.CASCADE_TUPLE:
            cascade = cv.Load(cascade)
            dos = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                         FaceFilter.HAAR_SCALE, FaceFilter.MIN_NEIGHBORS, FaceFilter.HAAR_FLAGS, FaceFilter.MIN_SIZE)
            dectected_objects.extend(dos)
        
        t = cv.GetTickCount() - t
        print "detection time = %gms" % (t/(cv.GetTickFrequency()*1000))
                
        if dectected_objects:
            for ((x, y, w, h), n) in dectected_objects:
                # the input to cv.HaarDetectObjects was resized, so scale the 
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * FaceFilter.IMAGE_SCALE), int(y * FaceFilter.IMAGE_SCALE))
                pt2 = (int((x + w) * FaceFilter.IMAGE_SCALE), int((y + h) * FaceFilter.IMAGE_SCALE))
                cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)

            cv.SaveImage( FaceFilter.PHOTO_PATH + 'filtered_photos/' + file_name, img)
                
    def process(self):
        for file in self.file_list:
            pass 
        
def main():
    
    file_list = os.listdir(FaceFilter.PHOTO_PATH)    
    
    ff = FaceFilter()
    
    #file_name = FaceFilter.PHOTO_PATH + 'a1.jpg'
    
    for file_name in file_list:
        exclude_strings = filter( lambda x: x if x in file_name else "", FaceFilter.EXCLUDE_STRING ) 
        
        if exclude_strings:
            continue
        if not os.path.isdir( FaceFilter.PHOTO_PATH + file_name):
            image = cv.LoadImage( FaceFilter.PHOTO_PATH + file_name, 1 )
            ff.dectect(image, file_name)
            
if __name__ == '__main__':main()

