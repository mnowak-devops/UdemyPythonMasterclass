import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")
content = webpage.content
result = BeautifulSoup(content, "html.parser")

#Searching the HTML tree
#The find() method - finds the first occurrence of a certain tag
#More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
print (result.find("h1"))

#The find_all() method - finds the all occurrences of a certain tag (and other features, e.g. class name)
#More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
print (result.find_all("div"))
print (result.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"}))


#More info on searching: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree