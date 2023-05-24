from bs4 import BeautifulSoup
import requests
import sys

# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')## in get method is the part we make use of encoding="utf-8"

url = "https://coinmarketcap.com/"
result = requests.get(url)
result.encoding = 'utf-8'  # Set the encoding of the response explicitly
doc = BeautifulSoup(result.text, "html.parser")


# how we can navigate over the html tree 
#   print(trs[0].next_sibling)
#   print(trs[1].previous_sibling)
#   print(trs[0].next_siblings)----this tend to provide all the information after the first one which is BITCOIN

# using the parent 
#  using .parent it tend to give us the above tags which in our case is the tbody
#                example of this is print(trs[0].parent.name)
# usind decendant in the search ---which provides information after the given data --afterwards
#                example of this print(list(trs[0].descendants))
#                 #--children #---descendants #--contents both of them are used the same way 




tbody = doc.tbody
trs = tbody.contents

# geting the prices of the cryptocurrencies 
#
# for tr in trs:
#    for td in tr.contents[2:4]:
#          print(td)
#

# for tr in trs[:10]:
#    name, price = tr.contents[2:4]
#    print(name.p.string)
#    print(price.a.string)


prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string


    prices[fixed_name] = fixed_price

print(prices)    
    
    
