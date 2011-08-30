'''
Created on Jul 21, 2011

@author: redbug
'''

def decorator_function_with_args(arg1, arg2, arg3):
    """
    decorator function(not decorator class)
    """
    
    def wrap(f):
        """
        wrap() can only take a single argument (the function object) and must return the decorated function object
         that replaces the original. Notice that wrap() is only invoked once.
        """
        print "Inside wrap()"
        
        
        def wrapped_f(*args):
            """
            wrapped_f() is the actual replacement function.
            """
            print "Inside wrapped_f()"
            print "Decorator arguments:", arg1, arg2, arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f
    return wrap


@decorator_function_with_args("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print "sayHello arguments:", a1, a2, a3, a4
    
print "After decoration"


print "Preparing to sayHello()"
sayHello("say", "hello", "argument", "list")
print "After first sayHello() call"
sayHello("a", "different", "set of", "arguements")
print "After second sayHello() call"
