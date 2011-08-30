#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open( 'lines.txt' )
    for index, line in enumerate( fh.readlines() ):
        print( index, line, end='' )

    str = "This is a string"
    for index, s in enumerate( str ):
        print( "index {} is s".format( index ) ) if s == "s" else {}

if __name__ == "__main__": main()
