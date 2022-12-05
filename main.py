import random

def func(p, str_az):
    for x in range(11):
        p += ''.join(random.choices(str_az))
    return p

p = ''
str_az = [chr(value) for value in range(ord('a'), ord('z'))]
res = func(p, str_az)
print(res)