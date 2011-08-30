#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    i = 0

    for c in s:
        if c == "s":
            continue
#        elif c == "g":
#            break

        print( c, end='' )

    else:
        print( "EOF" )


    for c in "Test for Break":
        if c == "B":
            break;
        else:
            print( c, end='' )
    else:
        print( "EOF" )


if __name__ == "__main__": main()
