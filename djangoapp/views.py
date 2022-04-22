from django.shortcuts import render
import pandas as pd
import requests


# Create your views here.


def index(request):
    return render(request, 'drop.html')


def home(request):
    return render(request, 'index.html')


def upload_file(request):
    file = request.FILES['filefield']
    df = pd.read_excel(file, engine='openpyxl')
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
    return render(request,'dropdown.html',{'allcolumns':list(df.columns)})
    company=request.POST['']
    first_name = request.POST['']
    last_name = request.POST['']
    phone = request.POST['']
    email = request.POST['']
    for index, row in df.iterrows():
        payload = [{
            "company": company,
            "first_name": first_name, 
            "last_name": last_name,
            "phone": phone,
            "email": email,
        }]
        print(payload)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
