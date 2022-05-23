from wsgiref.util import request_uri
from bs4 import BeautifulSoup
import requests
import csv

#get html
url = "https://buyersguide.macrumors.com/"

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# get all the products

Ios = soup.find(id="pane-ios").find_all('li')

Mac = soup.find(id="pane-mac").find_all('li')

Headphones = soup.find(id="pane-music").find_all('li')

Other = soup.find(id="pane-other").find_all('li')

All = Ios + Mac + Headphones + Other

# product = Ios[0]
# name = product.find('a').text
# status = product['class'][0]
# img = product.img['src']

# # print(product)
# print(name)
# print(status)
# print(img)


# CSV
csv_headers = ['Name', 'Status', 'Image']
with open('istheappleripe.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)


for product in All:
    name = product.find('a').text
    status = product['class'][0]
    img = product.img['src']
    with open('istheappleripe.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, status, img])

