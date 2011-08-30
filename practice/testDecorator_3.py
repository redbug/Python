'''
Created on Jul 21, 2011

@author: redbug

'''

def entry_exit(f):
    """
    decorator function(not decorator class)
    """
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    # new_f.__name__ = f.__name__  
    return new_f

@entry_exit
def func1():
    print "inside func1()"
    
@entry_exit    
def func2():
    print "inside func2()"
    
def main():
    func1()
    func2()
    print func1.__name__  # new_f
    
if __name__ == "__main__": main()