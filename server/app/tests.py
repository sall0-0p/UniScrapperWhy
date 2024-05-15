import requests
import json

responce = requests.get(f'http://127.0.0.1:5000/product/{input("Product ID: ")}', data={ 'update_data': False, 'only_meta': True, })

print(responce.json())
