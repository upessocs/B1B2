x = 10  # Global variable


def outer_function():
    
#    print(f"value of x in outer function {x}")
    x = 20  # Enclosing variable
    
    print(f"value of x in outer function after modification {x}")
    
    def inner_function():
#        print(f"value of x in inner function before modification is {x}")
        x = 30  # Local variable
        print(f"value in inner function after modification {x}")  # Output: 30

        
    inner_function()
    print(x)  # Output: 20





print(f"value of x in global scope before function execution {x}")  # Output: 10


outer_function()

print(f"value of x in global scope after function execution {x}")  # Output: 10




