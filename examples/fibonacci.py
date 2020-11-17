# find fibonacci
n = int(input("How many numbers display : "))
n1, n2 = 0, 1

if n <= 0:
    print("Please enter a positive numbers")
elif n == 1:
    print("Fibonacci sequence upto", n, " : ")
    print(n1)
else:
    print("\nFibonacci sequence : ")
    count = 0
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
