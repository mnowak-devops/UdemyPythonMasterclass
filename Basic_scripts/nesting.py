x = "Cisco"

if "i" in x:
    if len(x) > 3:
        print(x, len(x))


list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
        for j in list2:
            print (i * j)
        print(i)



y = 1

while y <= 10:
    z = 5
    y += 1
    while z <= 10:
        print(z)
        z += 1

for number in range(10):
    if 5 <= number <= 9:
        print (number)
