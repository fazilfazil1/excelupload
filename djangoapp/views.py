from django.shortcuts import render
import pandas as pd
import requests


# Create your views here.


def index(request):
    return render(request, 'drop.html')


def home(request, ):
    return render(request, 'index.html')


def next_page(request):
    return render(request, 'dropdown.html')


def upload_file(request):
    file = request.FILES['filefield']
    df = pd.read_excel(file, engine='openpyxl')
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
    company = request.POST['select']
    first_name = request.POST['select2']
    last_name = request.POST['select3']
    phone = request.POST['select4']
    email = request.POST['select5']
    addressfirst_name = request.POST['select6']
    city = request.POST['select7']
    country_code = request.POST['select8']
    addresslast_name = request.POST['select9']
    address1 = request.POST['select-10']
    postal_code = request.POST['select-11']
    state_or_province = request.POST['select-11']

    for index, row in df.iterrows():
        payload = [{
            "company": row[company],
            "first_name": row[first_name],
            "last_name": row[last_name],
            "phone": str(row[phone]),
            "email": row[email],
            "addresses": [
                {
                    "first_name": row[addressfirst_name],
                    "city": row[city],
                    "country_code": row[country_code],
                    "last_name": row[addresslast_name],
                    "address1": row[address1],
                    "postal_code": str(row[postal_code]),
                    "state_or_province": row[state_or_province]
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
        return render(request, 'dropdown.html', {'allcolumns': list(df.columns)})
