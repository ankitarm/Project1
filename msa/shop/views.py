from django.shortcuts import render
from .models import Product, Contact, Order
from math import ceil
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("shop page")
    # products = Product.objects.all()
    # print(products)

    # params={'no_of_slides': nSlide, 'product': products, 'range': range(1, nSlide) }
    allProducts = []
    categoryproducts = Product.objects.values('category', 'id')
    categorys = {item['category'] for item in categoryproducts}
    for cat in categorys:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod, range(1, nSlide),nSlide])
    params = {'allProducts':allProducts}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request, myid):
    # fetch product using id..
    prod = Product.objects.filter(id=myid)
    print(prod)
    # prod is list
    return render(request, 'shop/productview.html', {'prod':prod[0]})

def checkout(request):
    if request.method == "POST":

        inputname = request.POST.get('name', '')
        inputEmail4 = request.POST.get('email', '')
        inputAddress = request.POST.get('phone', '')
        inputAddress2 = request.POST.get('desc', '')
        inputCity = request.POST.get('name', '')
        inputState = request.POST.get('email', '')
        inputZip = request.POST.get('phone', '')
        phone= request.POST.get('desc', '')

        order = Order(inputname=inputname,inputEmail4=inputEmail4,inputAddress=inputAddress,inputAddress2=inputAddress2,inputCity=inputCity, inputState=inputState,inputZip=inputZip, phone=phone)
        order.save()
    return render(request, 'shop/checkout.html')
