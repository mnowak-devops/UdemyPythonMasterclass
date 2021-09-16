import re
a = "I enjoy learning programing languages such as Python 3"

print(re.search(r"^[A-Z]\s\w{5}", a))

print(re.search(r"[A-Z]\w{5}\s\d$", a))


x = "He is ... zzzzzzzzzz ... sleeeeeeping"

print(re.search(r"z{10}", x))

print(re.search(r"z{1,}", x))

print(re.search(r"z{1,10}", x))

print(re.search(r"z{1,10}?", x))

print(re.search(r"z{3,10}?", x))

