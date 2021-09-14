import re
a = "I enjoy learning programing languages sucha as Python 3"

print(re.split(r" ", a))

print(re.split(r"\s", a))

print(a.split(r" "))


print(re.split(r"\W\w{2}\W", a))


print(re.subn(r"\s", "_", a))