# from datetime import time
import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
# from . migrate import *
import pandas as pd
import requests
from .models import Customer

# Create your views here.
def home(request):
    return render(request,'index.html')
def upload_file(request):
    file = request.FILES['filefield']
    print(file)
    # fs = FileSystemStorage()
    # fname = time.strftime("%Y%m%d-%H%M%S") + ".xlsx"
    # file_name = fs.save(fname, file)
    # path = fs.url(file_name)
    #
    # cust_obj = Customer()
    # cust_obj.customers = path
    # cust_obj.save()
    # print('**', path)

    # file_obj=Customer.objects.all()
    # data=file_obj.customer
    df = pd.read_excel(file, engine='openpyxl')
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
    for index, row in df.iterrows():
        payload = [{
            "company": row['company'],
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "phone": str(row['phone']),
            "email": row['email'],
            "notes": row['notes'],
            "addresses": [{
                "address1": row['address1'],
                "address2": row['address2'],
                "address_type": row['addresstype'],
                "city": row['address_city'],
                "company": row['Company'],
                "country_code": row['addresscountry_code'],
                "first_name": row['addressfirst_name'],
                "last_name": row['address_last_name'],
                "phone": str(row['addressphone']),
                "postal_code": str(row['postal_code']),
                "state_or_province": row['state_or_province']
            }
            ]
        }]
        print(payload)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
    return home(request)

#     cust_obj.file=path
#     cust_obj.save()
#
#     print('**',path)
#     # df = pd.read_excel('file', engine='openpyxl')
#     # url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
#     # for index, row in df.iterrows():
#     #     payload = [{
#     #         "company": row['Company'],
#     #         "first_name": row['First Name'],
#     #         "last_name": row['Last Name'],
#     #         "phone": str(row['Phone']),
#     #         "email": row['Email'],
#     #         "notes": row['Note'],
#     #         "addresses": [{
#     #             "address1": row['address1'],
#     #             "address2": row['address2'],
#     #             "address_type": row['addresstype'],
#     #             "city": row['address_city'],
#     #             "company": row['company'],
#     #             "country_code": row['addresscountry_code'],
#     #             "first_name": row['addressfirst_name'],
#     #             "last_name": row['address_last_name'],
#     #             "phone": str(row['addressphone']),
#     #             "postal_code": str(row['postal_code']),
#     #             "state_or_province": row['state_or_province']
#     #         }
#     #         ]
#     #     }]
#     #     print(payload)
#     #     headers = {
#     #         "Content-Type": "application/json",
#     #         "Accept": "application/json",
#     #         "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
#     #     }
#     #     response = requests.request("POST", url, json=payload, headers=headers)
#     #     print(response.text)
#
#     return render(request, "index.html")