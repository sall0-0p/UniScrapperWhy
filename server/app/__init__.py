from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
from products import scraper
from pathlib import Path
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
            with open(item, 'r') as json_file:
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
            with open(item, 'r') as json_file:
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

api.add_resource(ProductList, '/products')
api.add_resource(ListMeta, '/product-meta')
api.add_resource(Product, '/product/<productId>')

app.run(port=5000)
