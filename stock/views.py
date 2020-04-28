from django.shortcuts import render
from .models import Product
from suds.client import Client
import xmltodict, json

#from django.http import HttpResponse

# Create your views here.
def index(request):
    
    products = Product.objects.all()

    #html="<html><body>Home page</body></html>"
    #return HttpResponse(html)
    return render(request,'frontend/index.html',{'products':products})

def about(request):
    
    tags = ['น้ำตก','ธรรมชาติ','หน้าฝน','ตากหมอก','คอมพิวเตอร์']
    data = {}
    
    data['nature'] = {
            'name':'บทความท่องเที่ยวภาคเหนือ',
            'author':'อำนวย ปิ่นทอง',
            'tags': tags
            }
    
    data['computer'] = {
            'name':'Django for Beginner..',
            'author':'John Doe'            
            }
        
    return render(request,'frontend/about.html',data)

def contact(request):
    
    client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
    OilPrice = client.service.CurrentOilPrice(Language='thai')
    #หากต้องการใช้ GetOilPrice ให้แก้เป็น client.service.GetOilPrice(รายละเอียดตามเอกสาร)
    #print(OilPrice)
    #print(type(OilPrice))
    OilPrice1 = xmltodict.parse(OilPrice) # ได้ผลลัพธ์เป็น json ในสตริง
    Prices = eval(json.dumps(OilPrice1)) # เรียกใช้งาน json ในสตริง
    #print(Prices)

    
    for v in Prices['PTTOR_DS'].items():
        for i in v:
            print(type(i))
    
    return render(request,'frontend/contact.html')