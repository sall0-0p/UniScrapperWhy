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

# print(scraper.getReviews('151755777', False))
# print(scraper.getReviews('150314826', False))

def checkIfExists(productId):
    return (data_folder / f'{productId}.json').exists()

class ProductList(Resource):
    def get(self):
        args = parser.parse_args()
        items = data_folder.iterdir()
        result = {}
        for item in items:
            with open(item, 'r') as json_file:
                data = json.load(json_file)
                if args['only_meta']:
                    result[item.stem] = data['meta']
                else:
                    result[item.stem] = data[item.stem]

        return json.dumps(result, indent=4, ensure_ascii=False)
    
    def delete(self):
        items = data_folder.iterdir()

        for item in items:
            item.unlink()
        return 204

class Product(Resource):
    def get(self, productId):
        args = parser.parse_args()
        data = scraper.getReviews(productId, args['update_data'])
        
        if args['only_meta']:
            data_json = json.loads(data)
            return json.dumps(data_json['meta'], indent=4, ensure_ascii=False)
        else:
            print(args)
            return data
        
    def delete(self, productId):
        file_path = data_folder / f'{productId}.json'
        if file_path.exists():
            file_path.unlink()
        else:
            abort(404, 'File does not exist!')
        return 204

api.add_resource(ProductList, '/')
api.add_resource(Product, '/product/<productId>')

app.run(port=5000)
