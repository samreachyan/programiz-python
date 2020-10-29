# Random generator
import random

print("You get random number : ", random.randint(0, 9))

term = 10
result = list(map(lambda x: 2 ** x, range(term)))

print("The total term are : ", term)
for i in range(term):
    print("2 raised to power ", i, ' is ', result[i])
