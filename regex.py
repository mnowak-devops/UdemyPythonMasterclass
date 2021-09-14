import re


mystr = "You can learn any programing language, wheter it is Python2, Python3, Perl, Java, javascript or PHP."



a = re.match("You", mystr)
print (a)


a = re.match("abc", mystr)
print (a)

print (type(a))


a = re.match("You", mystr)
print (a.group())


a = re.match("you", mystr, re.I)
print (a)
print (a.group())


mystry = " can learn you any programing language, wheter it is Python2, Python3, Perl, Java, javascript or PHP."

a = re.match("you", mystry, re.I)
print (a)
print (type(a))


arp = "22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222       L"

b = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*",arp)
print (b.group(1))
print (b.group(2))
print (b.group(3))
print (b.group(4))


print (b.groups())


c = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)

print (c)
print (type(c))


arp = "22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222   10.10.10.10    L"
c = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)

print (c)


arpd = "22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222       L"

d = re.sub(r"\d", "7", arpd)

print (d)