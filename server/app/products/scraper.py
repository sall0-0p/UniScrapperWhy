import requests
import os
import json
from products import utils
from products import analytics
from pathlib import Path
from bs4 import BeautifulSoup

mappingFunctions = {
    "recommendation": [utils.mapRecommendation, False],
    "score": [utils.mapScore, False],
    "helpful": [int, False],
    "unhelpful": [int, False],
}

path = Path(__file__)

def extract(ancestor, selector=None, attribute=None, return_list=False):
    if return_list:
        if attribute:
            result = [tag[attribute] for tag in ancestor.select(selector)]
        else:
            result = [tag.get_text().strip() for tag in ancestor.select(selector)]
        
        if len(result) > 0:
            return result
        else:
            return None
    if selector:
        if attribute:
            try:
                return ancestor.select_one(selector)[attribute]
            except TypeError:
                return None
        try:   
            return ancestor.select_one(selector).get_text().strip()
        except AttributeError:
            return None
    if attribute:
        return ancestor[attribute]
    return ancestor.get_text().strip()

def loadReviews(productId):
    all_opinions = []
    processed_opinions = 0
    url = "https://www.ceneo.pl/" + productId + "#tab-reviews"

    while(url):
        responce = requests.get(url)

        page_dom = BeautifulSoup(responce.text, "html.parser")
        opinions = page_dom.select("div.js_product-review")

        for opinion in opinions:
            single_opinion = {
                key: extract(opinion, *value)
                    for key, value in utils.selectors.items()
            }

            for key, value in mappingFunctions.items():
                if single_opinion.get(key) != None:
                    if value[1] == True:
                        single_opinion[key] = list(map(value[0], single_opinion[key]))
                    else:
                        single_opinion[key] = value[0](single_opinion[key])

            all_opinions.append(single_opinion)
            processed_opinions += 1
        try:
            url = "https://www.ceneo.pl/" + extract(page_dom, "a.pagination__next", "href")
        except TypeError:
            url = None
    return all_opinions, processed_opinions, page_dom

def getReviews(productId, update):
    pathToJson = path.parent.parent / 'data' / f'{productId}.json'

    if pathToJson.exists() and not update:
        with open(pathToJson, 'r') as json_file:
            return json_file.read()
    else:
        product, processed_opinions, page_dom = loadReviews(productId)
        analytics_result = analytics.getAnalytics(product)

        data = {
            "meta": {
                "productName": extract(page_dom, ".product-top__product-info__name"),
                "productId": productId,
                "reviewCount": processed_opinions,
                'icon': '../src/assets/images/brass_hand.png',
                # "icon": "https:" + extract(page_dom, ".js_gallery-media", "src"),
                "rating": analytics_result[3],
            },
            "content": product,
        }

        json_file = open(pathToJson, 'w')
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()
        
        return json.dumps(data, indent=4, ensure_ascii=False)

print(getReviews('151755777', False))
print(getReviews('150314826', False))
