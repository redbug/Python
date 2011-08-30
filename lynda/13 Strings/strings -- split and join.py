#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = "This is Redbug's speaking!"
    print( s.split( ' ' ) )
    print( s.split( 's' ) )
    splittedStr = s.split( ' ' )
    print( ' '.join( splittedStr ) )
    print( ':'.join( splittedStr ) )

if __name__ == "__main__": main()

