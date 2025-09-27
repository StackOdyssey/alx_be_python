import random

x = []
for i in range(10):
    num=random.randint(1, 10)
    print(num)
    x.append(num)
    print(x)
    print(type(x))
    x = set(x)
    print(x)
    print(type(x))