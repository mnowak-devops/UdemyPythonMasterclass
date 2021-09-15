import re
a = "I enjoy learning programing languages sucha as Python 3 "

result = re.search(r"\W(\w{2})\W|([A-Z]\w{5})\s\d", a)
print(result.group(1))

print(result.group(2))


result = re.search(r"\W(\w{50})\W|([A-Z]\w{5})\s\d", a)
print(result.group(1))

print(result.group(2))


"""
#Regular Expressions - the "re.match" and "re.search" methods
a = re.match(pattern, string, optional flags) #general match syntax; "a" is called a match object if the pattern is found in the string, otherwise "a" will be None

mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."

import re #importing the regular expressions module

a = re.match("You", mystr) #checking if the characters "You" are indeed at the beginning of the string

a.group() #result is 'You'; Python returns the match it found in the string according to the pattern we provided

a = re.match("you", mystr, re.I) #re.I is a flag that ignores the case of the matched characters

a = re.search(pattern, string, optional flags) #general search syntax; searching for a pattern throughout the entire string; will return a match object if the pattern is found and None if it's not found

arp = "22.22.22.1      0         b4:a9:5a:ff:c8:45 VLAN#222             L"


"""