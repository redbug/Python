#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open( 'lines.txt' )
    for line in fh.readlines():
        print( line, end='' )

    for s in "hello!":
        print( s )

if __name__ == "__main__": main()
