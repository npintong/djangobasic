from django.shortcuts import render
from .models import Product

#from django.http import HttpResponse

# Create your views here.
def index(request):
    
    products = Product.objects.all()

    #html="<html><body>Home page</body></html>"
    #return HttpResponse(html)
    return render(request,'frontend/index.html',{'products':products})

def about(request):
    return render(request,'frontend/about.html')

def contact(request):
    return render(request,'frontend/contact.html')