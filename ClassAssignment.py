# Write a program to estimate runtime of all the functions you have used so far.

import time as t
from functionScope import add as fn1
from functionScope import sub as fn2




def timeFunction(func,*args,**kwargs):#wrapper
    startTime = t.time()
    res = func(*args,**kwargs)
    endTime= t.time()
    runTimeInSec = endTime - startTime
    print(f"\n time to execute function is { runTimeInSec*1000000
     } micro seconds")


a = 10000
b = 20000

timeFunction(fn1,a,b)


timeFunction(fn2,a,b)


# for those who are unable to execute code and are late in assignment submissions and your git repo not updated regularly
# create a presentation to explain usage of passing function as arguments to modify function using wrapper functions