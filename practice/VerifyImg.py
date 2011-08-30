'''
Created on Mar 4, 2011

@author: redbug
'''
from PIL import Image
import os
photoPath = "/Users/redbug/Desktop/photos/" 
list = os.listdir(photoPath)

parsed =[]
for f in list:
    tokens = f.split('.')
    if not tokens[1] == "DS_Store" :
        print( "check: " + photoPath + f)
        image = Image.open(photoPath + f)
        try:
            print(image.verify())
        except:
            print("error")
        #parsed.append(f)
#print(parsed)        
