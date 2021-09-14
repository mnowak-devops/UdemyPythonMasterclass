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


