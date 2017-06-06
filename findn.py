'''
	code to find solutions 

'''

from timeit import Timer
import sys

filename = 'file'

def log(s):
    with open(filename, 'a') as f:
     f.write(s)
     f.close()

def find_invpow(x,n):
    """
		Finds the integer component of the n'th root of x,
    	an integer such that y ** n <= x < (y + 1) ** n.
    """
    low = 10 ** ((len(str(x)) - 1) / n)
    high = low * 10
    mid = 0

    while low < high:
        mid = (low + high) // 2
        midp = mid**n
        if low < mid and midp < x:
            low = mid
        elif high > mid and midp > x:
            high = mid
        else:
            return mid
    return mid + 1

def sump(li):
    l = len(li)
    #print l
    sum = 0
    for i in li:
       sum += i**l
    #print sum
    p = find_invpow(sum,l)
    flag = 0
    if (sum == p**l): 
        flag = 1
        s = str(flag) + ': ' +  str(li) + ' ' + str(sum) + ' ' + str(l) + ' ' + str(p) + '\n'
        log (s)
        print s
        sys.exit(0)
    return sum

def nth_num(num, depth, li):
    #print num, depth, li
    if (depth == 0):
        sum = sump(li)
        return

    for n in range (1, num+1):
        li0 = [x for x in li] 
        li0.insert(0,n)
        nth_num(n, depth-1, li0)

def work(n, d):
    li0 = [n]
    nth_num(n, d-1, li0)


a = sys.argv[1]
if sys.argv[2]: filename = sys.argv[2] 
depth = int(a)
#print depth
num = 1
while(1):
    s = str(num) + ' ' + str(depth)
    from datetime import datetime
    s += ' ' + str(datetime.now()) + '\n'
    log(s)
    work(num, depth)
    num += 1
