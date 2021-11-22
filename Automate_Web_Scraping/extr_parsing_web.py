
import requests

# Importing beautifulsoup4

from bs4 import BeautifulSoup

# Making a request / getting a webpage with Requests

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")

# The result is the Response object - I called it 'webpage'

print (type(webpage))

# Viewing the content as string

text = webpage.text
print (type(text))
print(text)
# Viewing the content as bytes

content = webpage.content
print (type(content))
print (content)
# Parsing the extracted webpage content using the default HTML parser


result = BeautifulSoup(text)
# or:
result = BeautifulSoup(content)
# or, also specifying the parser to use:
result = BeautifulSoup(content, "html.parser")

# The result is the BeautifulSoup object
print (type(result))