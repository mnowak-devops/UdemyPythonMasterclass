newfile = open ("newfile.txt", "w")

newfile.write("I like Pythone!\nDo you?\n")



newfile.writelines ({"Cisco\n", "Juniper\n", "HP\n"})



newfile = open ("newfile.txt", "a")

newfile.write("The file was appending")


newfile = open ("newfile.txt", "w+")

print (newfile.read())

