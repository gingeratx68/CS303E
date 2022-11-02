# CS 303E Quiz 3C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Root Parity Rule
def followsRule(num):
    """if True:
        math.sqrt(num)/2=abs 
    else:
        return False


def rangeOfNums(lower, upper):
    pass"""



# Problem 2: Phone Bill Class
class PhoneBill:
    # REMEMBER TO MAKE YOUR DATA MEMBERS PRIVATE
    def __init__(self, carrier, rate, minutes):
        self.__carrier=carrier
        self.__rate=rate
        self.__minutes=minutes

    def makeCall(self, minutes):
        self.__minutes=minutes

    def switchCarrier(self, carrier, rate):
        self.__carrier=carrier
        self.__rate=rate

    def getBill(self):
        return (self.__rate * self.__minutes)/100

    def __str__(self):
        return "The phone bill under %s for this month is $%.2f" % (self.__carrier, self.__rate)


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(followsRule(5))
    # print(followsRule(15))
    # print(rangeOfNums(0, 10))

    # pb = PhoneBill("TMobile", 67, 0)
    # print(pb.getBill())

    pb = PhoneBill("AT&T", 71, 530)
    pb.makeCall(20)
    print(pb)

    # pb = PhoneBill("Verizon", 72, 340)
    # pb.makeCall(15)
    # pb.switchCarrier("AT&T", 71)
    # pb.makeCall(15)
    # print(pb)

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
