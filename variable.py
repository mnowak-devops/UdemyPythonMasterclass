x = "Cisco"
y = " Switch"

print(x+y)
print(x*3)
print("o" in x)
print("b"not in x)
print("Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %f" % ("2601XM", 4, 12.3))
print("Cisco model: %s, %d WAN slots, IOS %f" % ("7200XM", 8, 15.4))
print("Cisco model: %s, %d WAN slots, IOS %.1f" % ("7200XM", 8, 15.4))
print("Cisco model: {0}, {1} WAN slots, IOS {2}".format("7200XM", 8, 15.4))
model = '2600Xm'
slots = 4
ios = 12.
print(f"Cisco model: {model}, {slots} WAN slots, IOS {ios}")
print(f"Cisco model: {model}, {slots * 2} WAN slots, IOS {ios}")
print(f"Cisco model: {model.lower()}, {slots * 2} WAN slots, IOS {ios}")

string1 = "O E2 10.110.8.9 [150/5] via 10.119.254.6, 0'01'00. Ethernet2"
print(string1)
print(string1[5: 15])
print(string1[5: 15])
print(string1[-1])
print(string1[-9: -1])
print(string1[-5: ])
print(string1[: -5])
print(string1[::2])
print(string1[::-1])