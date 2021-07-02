# Create your views here.
import time

from django.http import JsonResponse
import service


# Create your views here.
import user.register
import user.login
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


def user_register(request):
    name = "user" + str(time.time())
    if "name" in request.GET.keys():
        name = request.GET["name"]
    password = "password"
    if "password" in request.GET.keys():
        password = request.GET["password"]
    email = "email"
    if "email" in request.GET.keys():
        email = request.GET["email"]
    print("variables:[%s] [%s] [%s] " % (name, password, email))
    data = user.register.register_user(name, password, email)
    print(str(data))
    register_payload = {
        "code": 200,
        "message": "Success",
    }
    return JsonResponse(register_payload)


def user_login(request):
    name = "user" + str(time.time())
    if "name" in request.GET.keys():
        name = request.GET["name"]
    password = "password"
    if "password" in request.GET.keys():
        password = request.GET["password"]
    data = user.login.user_login(name, password)
    # todo: format data
    login_payload = {
        "code": 200,
        "message": "Success",
        "token": data
    }
    return JsonResponse(login_payload)
