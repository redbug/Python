#!/usr/bin/python

table = {}

def update_table(res_list, lookup):
    length = len(res_list)
    for index, n in enumerate(res_list):
        if not table.get(n):
            table[n]= length - index + lookup

def next(n):
    if n % 2 == 0:
        n = n >>1
    else:
        n = 3*n + 1
    return n

def L(n, acc=0, queue=[]):
    lookup = table.get(n)

    if lookup:
        update_table(queue, lookup)
        return acc + lookup
    else:
        queue.append(n)

    if n == 1:
        update_table(queue, 0)
        return 1 + acc
    else:
        return L(next(n), acc+1, queue)

def main():
    for i in range(1,101):
        print "L(%s) = %s" % ( i, L(i) )

if __name__ == "__main__": main()
