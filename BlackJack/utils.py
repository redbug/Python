#!/usr/bin/python2.6
"""
Black Jack - Utilities functions
"""
def check_float(num):
    try:
        num = float(num)
    except ValueError:
        return False, None
    else:
        return True, num

def check_int(num):
    try:
        num = int(num)
    except ValueError:
        return False, None
    else:
        return True, num
    
def message(msg):
    return  "-" + str(msg)

def print_error(msg):
    print "!! - " + str(msg)

def print_highlight(msg):
    print "*" + str(msg)

def print_action(msg):
    print "^" + str(msg)

def print_phase(phase):
    msg = "%s. %s" % (phase[0], phase[1])
    print "\n== " + msg +" ==" 