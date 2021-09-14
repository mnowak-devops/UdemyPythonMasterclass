import re
a = "I enjoy learning programing languages sucha as Python 3 "

result = re.findall(r"[a-z]",a)
print(result)

result = re.findall(r"[A-Z]",a)
print(result)

result = re.findall(r"[a-d]",a)
print(result)

result = re.findall(r"[abn]",a)
print(result)

result = re.findall(r"[^a]",a)
print(result)

result = re.findall(r"[0-9]",a)
print(result)

result = re.findall(r"[1-5]",a)
print(result)

result = re.findall(r"[135]",a)
print(result)


result = re.findall(r"[^7]",a)
print(result)