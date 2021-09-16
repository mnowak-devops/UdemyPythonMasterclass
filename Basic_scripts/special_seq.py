import re
a = "I enjoy learning programing languages sucha as Python 3 "

result = re.search(r"\D+", a)
print (result.group())

result = re.search(r"\S+", a)
print(result.group())

result = re.search(r"\W+", a)
print(result.group())
print(a.index(result.group()))

result = re.search(r"\AI", a)
print(result.group())