# Write a program to estimate runtime of all the functions you have used so far.

import time as t
from functionScope import add as fn1
from functionScope import sub as fn2




def timeFunction(func,*arg,**kwargs):#wrapper
    startTime = t.time()
    res = func(args,kwargs)
    endTime= t.time()
    runTimeInSec = endTime - startTime
    print(f"\n time to execute function is { runTimeInSec*1000000} micro seconds")


a = 1
b = 2

timeFunction(fn1,a,b,c=1)


timeFunction(fn2,a,b)


# for those who are unable to execute code and are late in assignment submissions and do not have any git repo update
# create a presentation to explain usage of passing function as arguments to modify function using wrapper functions