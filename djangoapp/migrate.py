# import pandas as pd
# import requests
#
# df = pd.read_excel('data.xlsx', engine="openpyxl")
#
# url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
#
# for index, row in df.iterrows():
#     payload = [{
#         "company": row['Company'],
#         "first_name": row['First Name'],
#         "last_name": row['Last Name'],
#         "phone": str(row['Phone']),
#         "email": row['Email'],
#         "addresses": [
#             {
#                 "first_name": row[' addressfirst_name'],
#                 "city": row['address_city'],
#                 "country_code": row['addresscountry_code'],
#                 "last_name": row['address_last_name'],
#                 "address1": row['address1'],
#                 "postal_code": str(row['postal_code']),
#                 "state_or_province": row['state_or_province']
#             }
#         ]
#     }]
#
#     print(payload)
#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
#     }
#     response = requests.request("POST", url, json=payload, headers=headers)
#     print(response.text)
