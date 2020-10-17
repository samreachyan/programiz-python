from fractions import Fraction as F
import math

print(F(1,3) + F(1,3))
print(1 / F(5, 6))
print(F(-3, 10) > 0)
print(F(-3, 10) < 0)

print(math.cos(math.pi * 2))


# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list[1])

x = [1, 2, 4, 3, 16, 32, 64, 128, 256, 512]

pow = [2 ** v for v in x] # pow = pow(2, x)
for i in pow: print(i)

## String
#Accessing string characters in Python
str = 'programiz'
print('str = ', str)
#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

