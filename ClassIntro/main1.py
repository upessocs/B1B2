from dog import Dog
from cat import Cat

from animal import Animal

dog1= Dog("d1",3)
cat1= Cat("c1",4)

print(dog1)
print(cat1)

print(isinstance(dog1,Dog))
print(isinstance(dog1,Cat))


print(isinstance(dog1,Animal))
print(isinstance(dog1,Animal))