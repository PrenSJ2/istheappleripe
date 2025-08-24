
from wsgiref.util import request_uri
from bs4 import BeautifulSoup
import requests
from app1.models import Products
import csv
from django.http import HttpResponse

def import_data():
    try:
        #get html
        iosUrl = "https://buyersguide.macrumors.com/#ios"
        macUrl = "https://buyersguide.macrumors.com/#mac"
        musicUrl = "https://buyersguide.macrumors.com/#music"
        otherUrl = "https://buyersguide.macrumors.com/#other"

        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

        iosPage = requests.get(iosUrl, headers=headers, timeout=10)
        macPage = requests.get(macUrl, headers=headers, timeout=10)
        musicPage = requests.get(musicUrl, headers=headers, timeout=10)
        otherPage = requests.get(otherUrl, headers=headers, timeout=10)
    except (requests.exceptions.RequestException, requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        print(f"Failed to fetch data from external source: {e}")
        # Add sample data when external source is unavailable
        create_sample_data()
        return HttpResponse("External data source unavailable. Using sample data.", status=200)

    try:
        iosSoup = BeautifulSoup(iosPage.content, 'html.parser')
        macSoup = BeautifulSoup(macPage.content, 'html.parser')
        musicSoup = BeautifulSoup(musicPage.content, 'html.parser')
        otherSoup = BeautifulSoup(otherPage.content, 'html.parser')

        # get all the products
        All = iosSoup.find_all("div", {"class": "guideContent--2FsbxzKc"})
        
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

        return HttpResponse(status=201)
        
    except Exception as e:
        print(f"Failed to parse HTML content: {e}")
        # Add sample data when parsing fails
        create_sample_data()
        return HttpResponse("Failed to parse external data. Using sample data.", status=200)


def create_sample_data():
    """Create sample Apple product data when external source is unavailable"""
    # First Delete all the items in the database
    Products.objects.all().delete()
    
    sample_products = [
        {
            'name': 'iPhone 15 Pro',
            'status': 'Buy Now',
            'status_info': 'Recently updated',
            'img': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-naturaltitanium-select?wid=470&hei=556&fmt=png-alpha&.v=1692895696418',
            'daysSince': '45',
            'avg': '365',
            'color': '#4CAF50'
        },
        {
            'name': 'MacBook Air M2',
            'status': 'Caution',
            'status_info': 'Mid-cycle',
            'img': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-midnight-select-20220606?wid=470&hei=556&fmt=png-alpha&.v=1653925212478',
            'daysSince': '180',
            'avg': '450',
            'color': '#FFC107'
        },
        {
            'name': 'iPad Pro M2',
            'status': "Don't Buy",
            'status_info': 'Update soon',
            'img': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipad-pro-12-select-wifi-spacegray-202210?wid=470&hei=556&fmt=png-alpha&.v=1664477502675',
            'daysSince': '300',
            'avg': '365',
            'color': '#F44336'
        }
    ]
    
    for product_data in sample_products:
        p = Products(
            name=product_data['name'],
            status=product_data['status'],
            status_info=product_data['status_info'],
            img=product_data['img'],
            daysSince=product_data['daysSince'],
            avg=product_data['avg'],
            color=product_data['color']
        )
        p.save()
        
        