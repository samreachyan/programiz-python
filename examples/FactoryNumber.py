# function of factorial
def print_factor(x):
    print("The factorial ",x ," are : ")
    for i in range(1, x+1):
        if x % i == 0:
            print(i)


num = 320
print_factor(num)
