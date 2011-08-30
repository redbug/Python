#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Egg():
    def __init__( self, kind="fried" ):
        self.kind = kind

    def whatKind( self ):
        print ( self.kind )

def main():
    fried_egg = Egg()
    fried_egg.whatKind()

    scrambled_egg = Egg( "Scrambled" )
    scrambled_egg.whatKind()

if __name__ == "__main__": main()
