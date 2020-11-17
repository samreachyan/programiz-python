from math import pi, e

for i in "samreach":
    if i == 'r': break
    print(i)

print("The end")

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul')


#lambda arguments: expression
double = lambda x : x * 2

# the same to 
'''
    def double (x):
        return x * 2
'''
print(double(4))

# new outer and inner function 
def outer():
    x = "local"

    def inner():
        nonlocal x 
        # when we assign type nonlocal to x mean this function will change value x
        # if you assign global to x, it will globally work outside function

        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("You can see e =", e)
print("Const pi =", pi)