# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
no_of_times = int(input('Enter the count: '))
position = (int(input('Enter the position: '))-1)
# Retrieve all of the anchor tags
i = 0
while i < no_of_times:
    bl_list = list()
    tags = soup('a')
    for tag in tags:
        h = (tag.get('href', None))
        bl_list.append(h)
    # print(bl_list[2])
    url = bl_list[position]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser') 
    x = bl_list[position].split('_')
    y = x[2].split('.')
    z = y[0]   
    i += 1
print(z)
    
    