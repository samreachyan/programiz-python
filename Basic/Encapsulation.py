class Computer:
    
    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print("Selling print {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# we cannot set value to maxprice
c.__maxprice = 1200
c.sell()

# set value to variable by method
c.setMaxPrice(1500)
c.sell()