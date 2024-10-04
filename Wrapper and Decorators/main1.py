# write a function that takes one input parameter (n) and evaluates an expression a = n * 10, for all values between 0 to n
import time
n = 1000000

def testfn(n):
    for i in range(0, n):
        a = i * 10

# extimate execution time of this function for n

start_time = time.time() * 1000000
print(start_time)

testfn(n)

end_time = time.time() * 1000000
print(end_time)
print(f"For n = {n} \nExecutin time is {end_time - start_time} micro seconds")

