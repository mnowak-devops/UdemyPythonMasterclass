import re

a = 'Last login: Tue Sep 21 20:57:38 2021 from 10.10.10.1\r\r\nenable\nterminal length 0\nArista3>enable\r\nArista3#terminal length 0\r\nPagination disabled.\r\nArista3#\r\nconfigure terminal\r\nArista3#configure terminal\r\nArista3(config)#show run\r\n! Command: show running-config\r\n! device: Arista3 (vEOS-lab, EOS-4.26.2F)\r\n!\r\n! boot system flash:/vEOS-lab.swi\r\n!\r\nno aaa root\r\n!\r\nusername admin role network-admin secret sha512 $6$uuWb7cXxlboV1gWZ$J8vtNNJpv8dUp1dcQZxbat0JRDkeFxRdrYLHXlSsUe27VW7S.AyK2g1lm5C4b7exmlfOf82EtcYlfutE37BPL.\r\n!\r\ntransceiver qsfp default-mode 4x10G\r\n!\r\nservice routing protocols model ribd\r\n!\r\nhostname Arista3\r\n!\r\nspanning-tree mode mstp\r\n!\r\ninterface Loopback0\r\nip address 3.3.3.3/24\r\n!\r\ninterface Management1\r\n   ip address 10.10.10.4/24\r\n!\r\nno ip routing\r\n!\r\nend\r\nArista3(config)#'

print(a)
# Split text into a list of elements
print(a.split('\r\n'))


b = a.split('\r\n')
# find the index of the element in the list
print(b.index('ip address 3.3.3.3/24'))

c = b[26]

print(c)

ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", c)

print (ip)
