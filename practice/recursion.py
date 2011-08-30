def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

def main():
    L = [1, 2, 3, 4, 5]
    sum = 0
    while L:
        print L
        sum += L[0] 
        L=L[1:]
    #print sum   

    print sumtree( [1, [2, [3, 4], 5], 6, [7,8]] )



if __name__ == "__main__": main()