a = lambda x, y: x * y

print(a)

print(type(a))

print(a(2, 10))

print(a(2, 50))


def my_func(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist

print(my_func([100, 101, 102]))

b = lambda mylist: [x *y for x in range(10) for y in range(5)] + mylist

print(b([100, 101, 102]))


"""
#Lambda functions - anonymous functions
lambda arg1, arg2, ..., arg n: an expression using the arguments #general syntax

a = lambda x, y: x * y #defining a lambda function

a(20, 10) #result is 200; calling the lambda function

#Instead of...
def myfunc(list):
    prod_list = []
    for x in range(10):
        for y in range(5):
            product = x * y
            prod_list.append(product)
    return prod_list + list

#...we can use a lambda function, a list comprehension and concatenation on a single line of code
b = lambda list: [x * y for x in range(10) for y in range(5)] + list

"""