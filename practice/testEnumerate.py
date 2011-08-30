'''
Created on Apr 13, 2011

@author: redbug
'''
str = "This is a string"
for index, s in enumerate( str ):
    if s == "s":
        print "index %s is s" % index
