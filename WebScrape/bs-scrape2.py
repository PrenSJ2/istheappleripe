from wsgiref.util import request_uri
from bs4 import BeautifulSoup
import requests
from app1.models
import csv

#get html
iosUrl = "https://buyersguide.macrumors.com/#ios"
macUrl = "https://buyersguide.macrumors.com/#mac"
musicUrl = "https://buyersguide.macrumors.com/#music"
otherUrl = "https://buyersguide.macrumors.com/#other"

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

iosPage = requests.get(iosUrl, headers=headers)
macPage = requests.get(macUrl, headers=headers)
musicPage = requests.get(musicUrl, headers=headers)
otherPage = requests.get(otherUrl, headers=headers)

iosSoup = BeautifulSoup(iosPage.content, 'html.parser')
macSoup = BeautifulSoup(macPage.content, 'html.parser')
musicSoup = BeautifulSoup(musicPage.content, 'html.parser')
otherSoup = BeautifulSoup(otherPage.content, 'html.parser')



# get all the products

Ios = iosSoup.find_all("div", {"class": "guideContent--2FsbxzKc"})

Mac = macSoup.find_all("div", {"class": "guideContent--2FsbxzKc"})

Headphones = musicSoup.find_all("div", {"class": "guideContent--2FsbxzKc"})

Other = otherSoup.find_all("div", {"class": "guideContent--2FsbxzKc"})

All = Ios + Mac + Headphones + Other

# Testing

# product = Ios[0]
# name = product.find_all('a')[0].text
# status = product.find('strong').text
# status_info = product.find_all('div', {"class": "statusCell--1FKTVtOd"})[1].text
# img = product.img['src']
# daysSince = product.find_all('span', {"class": "days--339vsFb0"})[0].text
# avg = product.find_all('span', {"class": "days--339vsFb0"})[1].text

# print(avg)

# CSV

# csv_headers = ['Name', 'Status', 'Status info', 'Image', 'Days since last release', 'Average']
# with open('istheappleripe2.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(csv_headers)


for product in All:
    name = product.find_all('a')[0].text
    status = product.find('strong').text
    status_info = product.find_all('div', {"class": "statusCell--1FKTVtOd"})[1].text
    img = product.img['src']
    daysSince = product.find_all('span', {"class": "days--339vsFb0"})[0].text
    avg = product.find_all('span', {"class": "days--339vsFb0"})[1].text
    
    # Adding to database

    p = Product(name=product.name, status = product.status, status_info = product.status_info, img = product.img, daysSince = product.daysSince, avg = product.avg)
    p.save()

    # Creating a CSV with the data
    # with open('istheappleripe2.csv', 'a', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([name, status, status_info, img, daysSince, avg])

    