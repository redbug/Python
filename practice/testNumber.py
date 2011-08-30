#!/usr/bin/python2.6
'''
Created on Apr 7, 2011

@author: redbug
'''

import sys

def main():
    a = 40
    printType( a )

    b = 40.0
    printType( b )

    #in python2.x this is integer division, while in python3.x this is float division  
    c = 40 / 9
    printType( c )

    #in python2.x this is as same as previous case, while in python3.x this is integer division 
    d = 40 // 9
    printType( d )

    e = round( 40 / 9, 2 )
    printType( e )

def printType( obj ):
    sys.stdout.write( str( obj ) )
    print ( ", type: %s" % type( obj ) )

if __name__ == "__main__": main()
