'''
Created on Nov 2, 2012

@author: redbug
'''

def retry(arg1, arg2, arg3):
    
    def wrap(f):
        print "Inside wrap()"

        def wrapped_f(*args):
            print "Inside wrapped_f()"
            f(*args)
            print "After f(*args)"
        return wrapped_f
    return wrap


def sayHello(a1, a2, a3, a4):
    print "sayHello arguments:", a1, a2, a3, a4
    

retry_dec = retry("hello", "world", 42)
retry_dec(sayHello)("a","b","c","d")
#sayHello_with_retry("a", "b", "c", "d")
