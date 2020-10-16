import math

drink = "available"
food = None

def menu(x):
    if x == drink: print(drink)
    else: print(food)

menu(drink)
menu(food)

a = 5
# we can see the type
print(a, "is of type :", type(a)) 

print(math.pi)

a = [1, 2, 3]
# Retried value and index in array
for i, v in enumerate(a):
    print(i, " :", v)

b = []
b = [ v * 2 for v in a]

for i in b: print(i)

# Object
d = {'name': 'Samreach', 'type': 'huma'} 
for key in d:
    print(key, ' :', d[key])
