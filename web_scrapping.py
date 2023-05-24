from bs4 import BeautifulSoup
import requests
import sys

# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')## in get method is the part we make use of encoding="utf-8"

url = "https://www.jumia.co.ke/"
result = requests.get(url)
result.encoding = 'utf-8'  # Set the encoding of the response explicitly
doc = BeautifulSoup(result.text, "html.parser")

product = doc.find_all(string="Phone Accessories")
parent = product[0].parent
print(parent)

#with open("index.html", "r") as f:
#    doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())


# modification of the title..////changing the title of the html 
#tag = doc.title
#tag.string = "Hello Yasmin"
#print(doc)


# findig all the tags in html 
#tags = doc.find_all("p")
#print(tags)

# Accessing the nested tags in tags
#tags = doc.find_all("p")[0]
#print(tags.find_all("b"))


