#!/usr/bin/python

table = {}

def update_table(res_list, lookup):
    length = len(res_list)
    for index, n in enumerate(res_list):
        if not table.get(n):
            table[n]= length - index + lookup

def L(n):
    result = table.get(n)
    if result:
        return result, "lookup L(%s)" % n
    else:
        return hailstone(n)

def hailstone(n):
    o_n = n
    result=[n]
    while n > 1:
        if n % 2 != 0:
            n = 3*n + 1
        else:
            n = n >> 1
        
        lookup = table.get(n)
        if lookup:
            update_table(result, lookup)
            result.append("lookup L(%s)" % n)
            return table[o_n], result
        else:
            result.append(n)
    update_table(result,0)
    return len(result)

def main():
    for i in range(1,101):
        print "L(%s) = %s" % ( i, L(i) )
    
if __name__ == "__main__": main()
