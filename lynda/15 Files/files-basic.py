#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #mode = r, w, a, r+(read and write), rt(read text), rb(read binary)
    f = open( 'lines.txt', 'rt' )

    #for line in f.readlines():
    for line in f:
        print( line, end='' )

if __name__ == "__main__": main()
