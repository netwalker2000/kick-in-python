# Create your views here.
import time

from django.http import JsonResponse
import service

from productApp.serializers import ProductBriefSerializer, PhotoSerializer


def query_product_list(request):
    """
    This API is for query the product list.
    """
    name = ""
    if "name" in request.GET.keys():
        name = request.GET["name"]
    category = ""
    if "category" in request.GET.keys():
        category = request.GET["category"]
    last_updated_at = 0
    if "last_updated_at" in request.GET.keys():
        last_updated_at = int(request.GET["last_updated_at"])
    limit = 15
    if "limit" in request.GET.keys():
        limit = int(request.GET["limit"])

    data = service.product_service(name, category, last_updated_at, limit)
    ret_payload = {
        "code": 200,
        "message": "Success",
        "products": [ProductBriefSerializer().convert_to_dict(product) for product in data]
    }
    return JsonResponse(ret_payload)


def query_product_detail(request, id):
    print("id from path variable: " + id)
    data = service.query_product_detail(id)
    photo_data = service.query_photos(id)
    ret_payload = {
        "code": 200,
        "message": "Success",
        "productInfo": ProductBriefSerializer().convert_to_dict(data[0]),
        "photos": [PhotoSerializer().convert_to_dict(photo) for photo in photo_data]
    }
    return JsonResponse(ret_payload)
