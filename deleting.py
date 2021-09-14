f = open ('ruters.txt', "r")

print (f.read())

f.seek(0)

print (len(f.read()))

f.close()

f = open ('ruters.txt', "r+")

f.truncate(8)

f.close()