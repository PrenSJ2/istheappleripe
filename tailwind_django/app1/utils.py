
from wsgiref.util import request_uri
from bs4 import BeautifulSoup
import requests
from app1.models import Products
import csv
from django.http import HttpResponse

def import_data():
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

    All = iosSoup.find_all("div", {"class": "guideContent--2FsbxzKc"})
    

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

    # First Delete all the items in the database
    Products.objects.all().delete()

    # Find each product
    for product in All:
        name = product.find_all('a')[0].text
        status = product.find('strong').text
        status_info = product.find_all('div', {"class": "statusCell--1FKTVtOd"})[1].text
        img = product.img['src']
        daysSince = product.find_all('span', {"class": "days--339vsFb0"})[0].text
        avg = product.find_all('span', {"class": "days--339vsFb0"})[1].text
        # set color based off product status
        if str(status) == str("Buy Now"):
            color = "#4CAF50"
        elif status == "Caution":
            color = "#FFC107"
        elif status == "Don't Buy":
            color = "#F44336"
        else:
            color = "gray"

        # Add to database
        p = Products(name=name, status = status, status_info = status_info, img = img, daysSince = daysSince, avg = avg, color=color)
        p.save()

        # # Creating a CSV with the data
        # with open('istheappleripe2.csv', 'a', encoding='utf-8', newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow([name, status, status_info, img, daysSince, avg])


    return HttpResponse(status=201)
        