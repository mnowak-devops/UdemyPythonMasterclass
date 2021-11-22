import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")
content = webpage.content
result = BeautifulSoup(content, "html.parser")


#Extracting webpage elements by tag

#Extracting the head - creates a Tag object
#Will return only the first tag by that name
head = result.head
print (type(head))


#Extracting h2 heading - creates a Tag object
#Will return only the first tag by that name
h2 = result.h2
print (type(h2))


#Extracting the title - creates a Tag object
#Will return only the first tag by that name
title = result.title
print (type(title))


#Accessing the name of a tag
print (head.name)

print (h2.name)

print (title.name)

#Setting a new name for a tag
title.name = "mytitle"
print (title)

#This change is reflected in the BeautifulSoup object itself

#A tag may have any number of attributes. Example:
#<header role="banner" class="navbar navbar-fixed-top navbar-static">
#The header tag has two attributes:
#attribute: role, value: "banner"
#attribute: class, value: "navbar navbar-fixed-top navbar-static"

#Using the attrs object attribute you can view the tag's own attributes
#as a dictionary with the attribute name as the key and attribute value(s) as the value
#Here, the 'role' attribute is a single-valued attribute
#and the 'class' attribute is a multi-valued attribute
#Note: for multi-valued attributes you get a list of the attribute's values as the dictionary value
header = result.header
print(header.prettify()) #pretty printing HTML code
print (header.attrs)

#Accessing the value of a tag's attribute (as with any other dictionary)
print (header['role'])

print (header['class'])


#or, using the get() method:
print (header.get('role'))

print (header.get('class'))

#Modifying a tag's attribute value
header['role'] = "something"
print (header.attrs)


#Adding a new tag attribute
header['new'] = "python"
print (header.attrs)

#Removing a tag attribute
del header['new']
print (header.attrs)

#Extracting the string from a tag
h2 = result.h2
print (h2)

print (h2.string)

print (type(h2.string))

#this is called a NavigableString
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigablestring

#Zooming in to a certain area of the HTML tree
#Using a tag name as an attribute will give you only the first tag by that name
#More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
print (result.header.div)
print (result.header.div.div.a)
print (result.header.div.div.a.button)