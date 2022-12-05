import random

def func(p, str_az, str_AZ):
    for x in range(11):
        p += ''.join(random.choices(str_az + str_AZ))
    return p

p = ''
str_az = [chr(value) for value in range(ord('a'), ord('z'))]
str_AZ = [chr(value) for value in range(ord('A'), ord('Z'))]
res = func(p, str_az, str_AZ)
print(res)
