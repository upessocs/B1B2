# write a program to create a list of squares of numbers from 0 to n using list comrehension
n = 50
res = [ x**2 for x in range(0,n) if x % 2 == 0  ]
print(res)


res2 = { x:x**2 for x in range(0,n) if x % 2 == 0  }
print(res2)

def flip_dictionary(d1):
    assert isinstance(d1,dict), "Input is not a dictionay"
    flipped = { val:key for key,val in d1.items() }

    return flipped

print(f"flipped dictionayr is \n { flip_dictionary(res2)}")

flip_dictionary(1)