from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from products import scraper
from pathlib import Path
import pandas as pd
import dicttoxml
import json

app = Flask(__name__)
api = Api(app)
path = Path(__file__)
data_folder = path.parent / 'data'

CORS(app, supports_credentials=True)

parser = reqparse.RequestParser()
parser.add_argument('only_meta', default=False, location='form')
parser.add_argument('update_data', default=False, location='form')

def checkIfExists(productId):
    return (data_folder / f'{productId}.json').exists()

class ProductList(Resource):
    def get(self):
        args = parser.parse_args()
        items = data_folder.iterdir()
        if args['only_meta']:
            result = []
        else:
            result = {}

        for item in items:
            with open(item, 'r', encoding="utf8") as json_file:
                data = json.load(json_file)
                if args['only_meta']:
                    result.append(data['meta'])
                else:
                    result[item.stem] = data

        return json.dumps(result, indent=4, ensure_ascii=False)
    
    def delete(self):
        items = data_folder.iterdir()

        for item in items:
            item.unlink()
        return 204
    
class ListMeta(Resource):
    def get(self):
        items = data_folder.iterdir()
        result = []

        for item in items:
            with open(item, 'r', encoding="utf8") as json_file:
                data = json.load(json_file)
                result.append(data['meta'])

        return json.dumps(result, indent=4, ensure_ascii=False)
    
class Product(Resource):
    def get(self, productId):
        args = parser.parse_args()
        data = scraper.getReviews(productId, False)
        
        if args['only_meta']:
            data_json = json.loads(data)
            return json.dumps(data_json['meta'], indent=4, ensure_ascii=False)
        else:
            return data
        
    def post(self, productId):
        scraper.getReviews(productId, True)
        
    def delete(self, productId):
        file_path = data_folder / f'{productId}.json'
        if file_path.exists():
            file_path.unlink()
        else:
            abort(404, 'File does not exist!')
        return 204
    
class DownloadFile(Resource):
    def get(self, productId, format_type):
        print(f"Download for {productId} with type {format_type}")
        file_path = data_folder / f'{productId}.json'

        with open(file_path) as file:
            data = json.load(file)
            content = data['content']

        if content:
            if format_type == 'CSV':
                df = pd.json_normalize(content)
                response_data = df.to_csv(index=False)
                response = app.response_class(response=response_data, mimetype='text/csv')
                response.headers.set('Content-Disposition', 'attachment', filename='file.csv')
            elif format_type == 'XML':
                response_data = dicttoxml.dicttoxml(content)
                response = app.response_class(response=response_data, mimetype='application/xml')
                response.headers.set('Content-Disposition', 'attachment', filename='file.xml')
            else:
                response = jsonify(content)
                response.headers.set('Content-Disposition', 'attachment', filename='file.json')

            return response
        else:
            abort(404, 'File does not exist!')
        

api.add_resource(ProductList, '/products')
api.add_resource(ListMeta, '/product-meta')
api.add_resource(Product, '/product/<productId>')
api.add_resource(DownloadFile, '/download/<productId>/<format_type>')

app.run(port=5000)
