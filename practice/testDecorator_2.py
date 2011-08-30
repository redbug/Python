'''
Created on Jul 21, 2011

@author: redbug
'''

class entry_exit(object):
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@entry_exit        
def func1():
    print "inside func1()"

@entry_exit    
def func2():
    print "inside func2()"
    

def main():
    func1()
    func2()

if __name__ == "__main__": main()