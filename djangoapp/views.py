from urllib import request
from webbrowser import get
from django.shortcuts import render
import pandas as pd
import requests

# Create your views here.
# global variable
a = ''


# home page
def index(request):
    return render(request, 'drop.html')


# customer upload page
def customer(request):
    return render(request, 'index.html')


# customer upload file read and mapping the excel heading column with bigcommerce name
def upload_file(request):
    global a
    file = request.FILES['filefield']
    df = pd.read_excel(file, engine='openpyxl')
    a = df
    return render(request, 'dropdown.html', {'allcolumns': list(df.columns)})


# used to upload customer data to bigcommerce
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


# product upload page
def product(request):
    return render(request, 'productupload.html')


# used product file read and then upload to bigcommerce

# jsonData1 = {}
#
# jsonData1['name'] = row["Product Name"]
# jsonData1['sku'] = str(row['SKU'])
# jsonData1['type'] = row['Product Type']
# jsonData1['price'] = row['Default Price']
# jsonData1['weight'] = row['Weight ']
# jsonData1['description'] = row['Description']
# jsonData1['width'] = row['Width']
# jsonData1['depth'] = row['Depth']
# jsonData1['height'] = row['Height']
# jsonData1['cost_price'] = row['Cost']
# jsonData1['retail_price'] = row['MSRP']
# jsonData1['sale_price'] = row['Sale Price']
# jsonData1['map_price'] = row['map_price']
# jsonData1['tax_class_id'] = row['tax_class_id']
# jsonData1['product_tax_code'] = row['product_tax_code']
# # jsonData1['brand_id'] = row['brand_id']
# jsonData1['inventory_level'] = row['inventory_level']
# jsonData1['inventory_warning_level'] = row['inventory_warning_level']
# jsonData1['inventory_tracking']=row['inventory_tracking']
# jsonData1['fixed_cost_shipping_price'] = row['fixed_cost_shipping_price']
# jsonData1['is_free_shipping'] = row['is_free_shipping']
# jsonData1['is_visible'] = row['is_visible']
# jsonData1['is_featured']


def uploadproduct_file(request):
    file = request.FILES['filefield']
    df = pd.read_excel(file, engine='openpyxl')
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/catalog/products"
    for index, row in df.iterrows():
        payload = {
            "fixed_cost_shipping_price": row["fixed_cost_shipping_price"],
            "is_free_shipping": bool(row["is_free_shipping"]),
            "is_visible": bool(row["is_visible"]),
            "is_featured": bool(row["is_featured"]),
            "warranty": row["warranty"],
            "bin_picking_number": row["bin_picking_number"],
            "layout_file": row["layout_file"],
            "upc": row["upc"],
            "search_keywords": row["search_keywords"],
            "availability": row["availability"],
            "availability_description": row["availability_description"],
            "gift_wrapping_options_type": row["gift_wrapping_options_type"],
            "sort_order": row["sort_order"],
            "condition": row["condition"],
            "is_condition_shown": bool(row["is_condition_shown"]),
            "order_quantity_minimum": row["order_quantity_minimum"],
            "order_quantity_maximum": row["order_quantity_maximum"],
            "page_title": row["page_title"],
            "meta_keywords": [
                row["meta_keywords"]
            ],
            "meta_description": row["meta_description"],
            "view_count": row["view_count"],
            "preorder_release_date": row["preorder_release_date"],
            "preorder_message": row["preorder_message"],
            "is_preorder_only": bool(row["is_preorder_only"]),
            "is_price_hidden": bool(row["is_price_hidden"]),
            "price_hidden_label": row["price_hidden_label"],
            "open_graph_type": row["open_graph_type"],
            "open_graph_title": row["open_graph_title"],
            "open_graph_description": row["open_graph_description"],
            "open_graph_use_meta_description": bool(row["open_graph_use_meta_description"]),
            "open_graph_use_product_name": bool(row["open_graph_use_product_name"]),
            "open_graph_use_image": bool(row["open_graph_use_image"]),
            "brand_name or brand_id": row["brand_name or brand_id"],
            "gtin": row['gtin'],
            "mpn": row['mpn'],
            "custom_fields": [
                {
                    # "id": row['id'],
                    "name": row['Custom Field Name1'],
                    "value": row['Custom Field Value1']
                },
                {
                    # "id": row['id'],
                    "name": row['Custom Field Name2'],
                    "value": row['Custom Field Value2']
                },
                {
                    # "id": row['id'],
                    "name": row['Custom Field Name3'],
                    "value": row['Custom Field Value3']
                },
                {
                    # "id": row['id'],
                    "name": row['Custom Field Name4'],
                    "value": row['Custom Field Value4']
                }
            ],
            "bulk_pricing_rules": [
                {
                    # "id": row['bulkid'],
                    "quantity_min": row['quantity_min'],
                    "quantity_max": row['quantity_max'],
                    "type": row['type'],
                    "amount": row['amount']
                }
            ],
            "images": [
                {
                    "is_thumbnail": True,
                    "image_url": row['image_url'],
                    "description": row['imagedescription']
                }
            ],
            "videos": [
                {
                    "title": row["videotitle"],
                    "description": row["videodescription"],
                    "type": row["typevideo"],
                }
            ]
        }

        print(payload)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
    return render(request, 'drop.html')


# order upload page
def order(request):
    return render(request, 'orderupload.html')


# used to read order file and upload  to bigcommerce
def uploadorder_file(request):
    file = request.FILES['filefield']
    df = pd.read_excel(file, engine='openpyxl')
    url = " https://api.bigcommerce.com/stores/b5ajmj9rbq/v2/orders"
    for index, row in df.iterrows():
        payload = {
            "billing_address": {
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "street_1": row["Streename"],
                "city": row["city"],
                "state": row["state"],
                "zip": row["zip"],
                "country": row["country"],
                "country_iso2": row["country_iso2"],
                "email": row["email"]
            },
            "products": [
                {
                    "name": row["name"],
                    "quantity": row["quantity"],
                    "price_inc_tax": row["price_inc_tax"],
                    "price_ex_tax": row["price_ex_tax"]
                }
            ]
        }
        print(payload)
        headers = { 
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
    return render(request, 'drop.html')


# running background process
def backgroundprocess_file(request):
    # run background code here
    # fetch 10 bigcommerce product details one by one
    getbcproducts(request)
    return render(request,'background.html')
    

def getbcproducts(request):
     for i in range(10):
        url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/catalog/products/?limit=1"
        headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("GET", url, headers=headers)
        print(response.text)

  


