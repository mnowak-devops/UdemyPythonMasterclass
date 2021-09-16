myfile = open ("ruters.txt", "r")

print (myfile.mode)

print(myfile.read()) 

print(myfile.read(5))

print (myfile.seek(0))
print (myfile.tell())


print (myfile.read(5))

myfile.seek(0)

print (myfile.readline())
print (myfile.readline())
print (myfile.readline())
print (myfile.readline())
print (myfile.readline())
print (myfile.readline())
print (myfile.readline())
print (myfile.readline())


myfile.seek(0)

print (myfile.readlines(0))


myfile.seek(0)

for line in myfile.readlines():
    if line.startswith("A"):
        print (line)



myfile2 = open ("routers2.txt", "x")