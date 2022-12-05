import random

def func(p, str_az, str_AZ, str_09):
    for x in range(11):
        p += ''.join(random.choices(str_az + str_AZ + str_09))
    return p

p = ''
str_az = [chr(value) for value in range(ord('a'), ord('z'))]
str_AZ = [chr(value) for value in range(ord('A'), ord('Z'))]
str_09 = [str(value) for value in range(9)]
res = func(p, str_az, str_AZ, str_09)
print(res)
