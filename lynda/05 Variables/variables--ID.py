#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a = 10
    printId( a )

    a = 20
    printId( a )

    a = 10
    printId( a )

def printId( obj ):
    print ( obj, end='' )
    print ( ", id: %s" % id( obj ) )

if __name__ == "__main__": main()
