#!/usr/bin/python3

a,b = 1,3
if a < b:
    print('a ({}) is less than b ({}) {}'.format(a, b, 'redbug'))
else:
    print('a ({}) is not less than b ({}) {}'.format(a, b, 'redbug'))

print ("foo" if a<b else "redbug")
