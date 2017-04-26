# Peter Yang
# ITP 115, Spring 2017
# Lab 14
# yangpete@usc.edu


from Coffee import Coffee

maxOrders = 5
class Barista():
    def __init__(self, name):
        self.__name = name
        self.__orders = []
    def takeOrder(self):
        size = input("What size do you want? [small, medium, large]")
        desc = input("What type of drink are you ordering?")
        name = input("What is your name?")
        order = Coffee(size, desc, name)
        self.__orders.append(order)
        print(order)
    def isAcceptingOrders(self):
        return len(self.__orders) < maxOrders
    def makeDrinks(self):
        for order in self.__orders:
            order.setCompleted()
            print(order)
        self.__orders = []
    def __str(self):
        return "Hi! I am your barista and my name is " + self.__name