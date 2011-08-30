#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d1 = {"one":1, "two":2, "three":3, "four":4, "five":5 }

    print( "iterate d1 magically: " )
    iterate( d1 )

    print( "Iterate alphabetically:" )
    iterateKeySetAlphabetically( d1 )

# invalid because one, two, three and four are considered as variables by compiler
#    d2 = {one:1, two:2, three:3, four:4 }
#    iterate( d2 )

    d3 = dict( one=1, two=2, three=3, four=4, five=5 )

    print( "iterate d3 magically: " )
    iterate( d3 )

    print( "Iterate alphabetically: " )
    iterateKeySetAlphabetically( d3 )

def iterate( ob ):
    for o in ob:
        print( o, ob[o], end=' ' )
    print()

def iterateKeySetAlphabetically( ob ):
    for o in sorted( ob.keys() ):
        print( o, ob[o], end=' ' )
    print()


if __name__ == "__main__": main()
