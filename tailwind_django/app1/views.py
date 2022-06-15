from django.shortcuts import render
from app1.models import Products
from django.http import HttpResponse

# from tailwind_django.app1.utils import import_data

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def home(request):
    # import_data()
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def searchAjax(request, q):
    print(q)
    productList=Products.objects.filter(title__contains=q)
    n=len(productList)
    print(n)
    if (n>0):
        out=""
        for x in productList:
            out+="<h1 class='text-3xl'>" + x.name + "</h1><img class='h-30 w-30' src = '" + x.img + "'><p class='text-xl'>" + x.status + " | " + x.status_info + "</p><p class='text-md'>days since updated " + x.daysSince + "</p><p class='text-md'>average days between releases " + x.avg + " </p>"
    else:
        out="no matching results"
    print(out)
    return HttpResponse(out)