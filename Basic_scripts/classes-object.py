class MyRouter(object):
    "This is a router characteristics."
    def __init__(self, routername, model, serialno, ios ):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is; ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combine: ", self.model + manuf_date)


router1 = MyRouter('R1', '2600', '123456', '12.4')

print(router1.model)
print(router1.ios)
print(router1.serialno)
print(router1.routername)

router1.print_router("20181010")


router2 = MyRouter('R2', '7200', '101020', '12.2')

print(router1.ios)

router2.print_router("20190101")

router2.ios = "12.3"

print(getattr(router2, "ios"))

setattr(router2, "ios", "12.1")

print(getattr(router2, "ios"))

print(hasattr(router2, "ios"))
print(hasattr(router2, "ios2"))

delattr(router2, "ios")
print(hasattr(router2, "ios"))
#print(getattr(router2, "ios"))


print(isinstance(router2, MyRouter))


class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serialmo, ios, portsno):
        MyRouter.__init__(self,routername, model, serialmo, ios)
        self.portno = portsno

    def print_new_router(self, string):
        print(string + self.model)

new_router1 = MyNewRouter("newr1", "1800", "1111111", "12.2", "10")

print(new_router1.portno)
print(new_router1.model)
new_router1.print_router("ahajdlakdaj")
new_router1.print_new_router("ahajdlakdaj")

print(issubclass(MyNewRouter, MyNewRouter))


"""
#Classes and objects
class MyRouter(object): #creating a class which inherts from the default "object" class
    def __init__(self, routername, model, serialno, ios): #class constructor; initializing some variables and the method is called whenever you create a new instance of the class
        self.routername = routername #"self" is a reference to the current instance of the class
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)

router1 = MyRouter('R1', '2600', '123456', '12.4') #creating an object by simply calling the class name and entering the arguments required by the __init__ method in between parentheses

router1.model #accessing the object's attributes; result is '2600'

router1.print_router("20150101") #accessing a function (actually called method) from within the class
The router name is:  R1
The router model is:  2600
The serial number of:  123456
The IOS version is:  12.4
The model and date combined:  260020150101

getattr(router2, "ios") #getting the value of an attribute

setattr(router2, "ios", "12.1") #setting the value of an attribute

hasattr(router2, "ios") #checking if an object attribute exists

delattr(router2, "ios") #deleting an attribute

isinstance(router2, MyRouter) #verifying if an object is an instance of a particular class

class MyNewRouter(MyRouter): #creating a new class (child) inheriting from the MyRouter parent class
    ...

issubclass(MyNewRouter, MyRouter) #returns True or False; checking if a class is the child of another class

"""
