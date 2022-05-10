from django.shortcuts import render
import pandas as pd
import requests

# Create your views here.

a = ''


def index(request):
    return render(request, 'drop.html')


def home(request, ):
    return render(request, 'index.html')


def upload_file(request):
    global a
    file = request.FILES['filefield']
    df = pd.read_excel(file, engine='openpyxl')
    a = df
    return render(request, 'dropdown.html', {'allcolumns': list(df.columns)})


def read_file(request):
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
    company = request.POST['select0']
    first_name = request.POST['select1']
    last_name = request.POST['select2']
    phone = request.POST['select3']
    email = request.POST['select4']
    address1 = request.POST['select-10']
    address_city = request.POST['select7']
    country_code = request.POST['select8']
    addresses_first = request.POST['select5']
    address_lname = request.POST['select9']
    postal_code = request.POST['select-11']
    state_or_province = request.POST['select-12']

    for index, row in a.iterrows():
        payload = [{
            "company": row[company],
            "first_name": row[first_name], 
            "last_name": row[last_name],
            "phone": str(row[phone]),
            "email": row[email],
            "addresses": [
                  {
                    "first_name": row[addresses_first],
                    "city": row[address_city],
                    "country_code": row[country_code],
                    "last_name": row[address_lname],
                    "address1": row[address1],
                    "postal_code": str(row[postal_code]),
                    "state_or_province": row[state_or_province],
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
    return render(request, 'drop.html')

