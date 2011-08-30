'''
Created on Jul 8, 2011

@author: redbug
'''


import threading, Queue
import time
import random

NUM_THREADS = 10
Pool = Queue.Queue( 0 ) # the queue size is infinite.


class HitThread( threading.Thread ):

    def run( self ):
        time.sleep( random.randint( 1, 2 ) )
        
        target = Pool.get()
        
        if target:
            print target
            Pool.task_done()
                
                
                


for x in range( NUM_THREADS ):
    HitThread().start()


def main():
    for i in range(10):
        Pool.put( str(i) )


if __name__ == '__main__': main()
