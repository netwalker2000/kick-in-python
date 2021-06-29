import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import service


# Create your views here.
from productApp.serializers import ProductBriefSerializer


@api_view(
    ['GET']
)
def query_product_list(request):
    """
    This API is for query the product list.
    """
    name = ""
    if "name" in request.query_params.keys():
        name = request.query_params["name"]
    category = ""
    if "category" in request.query_params.keys():
        category = request.query_params["category"]
    last_updated_at = 0
    if "last_updated_at" in request.query_params.keys():
        last_updated_at = int(request.query_params["last_updated_at"])
    limit = 15
    if "limit" in request.query_params.keys():
        limit = int(request.query_params["limit"])

    service.product_service(name, category, last_updated_at, limit)
    return JsonResponse({"code": 200, "message": "Success"})


@api_view(
    ['GET']
)
def query_product_detail(request, id):
    print("id from path variable: " + id)
    data = service.query_product_detail(id)
    product_payload = {"products": [ProductBriefSerializer().convert_to_dict(product) for product in data]}
    return JsonResponse(product_payload)


@api_view(
    ['GET', 'POST']
)
def comments(request, id):
    print("id from path variable: " + id)
    if request.method == 'GET':
        print("geeeeeet")
    else:
        print("poooooooooost")
    return JsonResponse({"code": 200, "message": "Success"})
