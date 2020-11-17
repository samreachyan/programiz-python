class Complex:

    def __init__(self, r=0, i=0):
        self.real = r
        self.image = i

    def get_data(self):
        print(f'{self.real} + {self.image}j')

# create new complex 
num1 = Complex(2,5)

num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = Complex(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.image, num2.attr))
print(num2.attr)