from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from json import loads
import requests
from api.reciommender import recommend_products

@api_view(['GET'])
def get_recommendations(
    request,
    brand_id,
):
   
    beUrl = os.environ.get('NEXTJS_URL')
    resp_target_product = requests.get( beUrl +"/api/brands/"+str(brand_id))
    target_product_json = resp_target_product.json()
    rec = recommend_products(brand_id)
    response_data = {
        "target" : target_product_json,
        "top_4" : loads(rec.to_json(orient='records'))
    }
    return Response(response_data, status=200)
    

