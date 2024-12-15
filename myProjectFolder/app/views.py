import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

df = pd.read_csv(r'C:\Users\Aryan\Documents\Projects\web-scrapping\products.csv')

# Create your views here.
def index(request):
    html_page = "app/index.html"
    return render(request, html_page)

def home(request):
    return HttpResponse("From Home")

def product_grid(request):

    products = df[['id', 'product_name', 'image_url']].to_dict(orient='records')
    html_page = 'app/product_grid.html'
    return render(request, html_page, {'products': products})

def product_details(request, product_id):
    html_page = 'app/product_details.html'
    product = df[df['id'] == product_id].to_dict(orient='records')

    if product:
        product = product[0]
    else:
        product = None
    
    return render(request, html_page, {'product':product})