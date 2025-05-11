def sum(n):
    return

#Space complexity: 0(1), Auxllary space =0(1) Linear space:

def arraysum(a):
    sum=0
    for i in a:
        sum = sum + 1

    return

a = {12, 3, 4, 15}
arraysum(a)

# with the size of the array, the space also required increases.

#Space complexity: 0(n), Auxillary space = 0(1)

def sum(n):
    if(n<=0):
        return
    return n+ sum(n-1)

#space complexity: 0(n * n), Auxillary space = 0(n)