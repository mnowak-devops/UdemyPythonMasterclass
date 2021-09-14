import re
a = "I enjoy learning programing languages sucha as Python 3 "

result = re.search(r"\W(\w{2})\W|([A-Z]\w{5})\s\d", a)
print(result.group(1))

print(result.group(2))


result = re.search(r"\W(\w{50})\W|([A-Z]\w{5})\s\d", a)
print(result.group(1))

print(result.group(2))