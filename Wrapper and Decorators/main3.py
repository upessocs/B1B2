# write a function that takes one input parameter (n) and evaluates an expression a = n * 10, for all values between 0 to n
import time
ns = [12312312, 23423423, 24234234,234534]
n = 1000000



# def wrapper(func,n):
def wrapper(func, *args, **kwargs):
    def wrapped(*args, **kwargs):
        start_time = time.time() * 1000000

        func(*args, **kwargs)

        end_time = time.time() * 1000000
        print(f"For n = {n} \nExecutin time is {end_time - start_time} micro seconds")

    return wrapped


# main function
@wrapper # decorator
def testfn(n):
    for i in range(0, n):
        a = i * 10

@wrapper
def random1(n):
    n**n

random1(n)

# wrapped_fn  =  wrapper(testfn,n)
# wrapped_fn(n)


testfn(n)

# usefull while using fastapi for web server or api server