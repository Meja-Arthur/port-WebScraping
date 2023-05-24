from bs4 import BeautifulSoup
import requests
import sys
import re






with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# using regular expression in find an element 

#tags = doc.find_all(string=re.compile("\$.*"))

# how to save the changes made to our codes 
tags = doc.find_all('input', type="text")
for tag in tags:
    tag['placeholder'] = "i changed You "
# how to save the changes now 
with open('change.html', 'w') as file:
    file.write(str(doc))

#tag = doc.find_all(class_="btn-item")  # the method of finding a class in html 
#tag = doc.find_all(["option"], string="Undergraduate")  # finding of specific elements in the html code with additional information

#tag = doc.find(["div", "p", "li"])   searching for multiple tags in the query 

#tag["color"] = "blue"
#tag["selected"] = "false"   modification of attributes in the html 
#tag["value"] = "yasmin"   

