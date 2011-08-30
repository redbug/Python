#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a = 40
    printType( a )

    b = 40.0
    printType( b )

    c = 40 / 9
    printType( c )

    d = 40 // 9
    printType( d )

    e = round( 40 / 9, 2 )
    printType( e )

def printType( obj ):
    print ( obj, end='' )
    print ( ", type: {}".format( type( obj ) ) )

if __name__ == "__main__": main()
