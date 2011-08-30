#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open( 'raven.txt' )

    match = re.compile( '(Len|Neverm)ore', re.IGNORECASE )
    for line in fh:
        #compile once and be used many times, it is more efficiency.
        if re.search( match, line ):
            print( match.sub( '###', line ), end='' )

if __name__ == "__main__": main()
