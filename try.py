for i in range(5):
    try:
        print (i / 0)
    except ZeroDivisionError as e:
        print (e, "--> Division by 0 is not allowed, sorry!")



#for i in range(5):
 #   try:
 #       print (i / 0)
 #   except NameError:
 #       print ("You have a name error in your code!")




for i in range(5):
    try:
        print (i / 1)
    except ZeroDivisionError as e:
        print (e, "--> Division by 0 is not allowed, sorry!")
    print ("The rest of the code...")




for i in range(5):
    try:
        print (i / 1)
    except ZeroDivisionError as e:
        print (e, "--> Division by 0 is not allowed, sorry!")
    except NameError:
        print ("Name error detected!")
    except ValueError:
        print ("Wrong value!")



try:
    print (4 / 2)
except NameError:
    print ("Name Error!")
else:
    print ("No exceptions raised by try block!")


try:
    print (4 / 0)
except ZeroDivisionError:
    print ("Not allowed!")
finally:
    print ("I am steel going to be printed")    