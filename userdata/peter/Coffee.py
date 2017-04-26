# Peter Yang
# ITP 115, Spring 2017
# Lab 14
# yangpete@usc.edu

class Coffee():
    statuses = ["ordered", "completed"]
    def __init__(self, size, desc, name):
        self.__size = size
        self.__desc = desc
        self.__customer = name
        self.__status = 0
    def setCompleted(self):
        self.__status = 1
    def __str__(self):
        status = self.__customer + ", your order is complete" \
            if self.__status == 1 \
            else self.__customer + ", your order is in queue"
        status = "\n" + status
        return "Size: " + self.__size + ", Description: " + self.__desc + status