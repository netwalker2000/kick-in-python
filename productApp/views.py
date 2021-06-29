from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import service


# Create your views here.

@api_view(
    ['GET']
)
def query_list_no_param(request):
    service.product_service()
    return JsonResponse({"code": 200, "message": "Success"})


@api_view(
    ['GET']
)
def query_product_detail(request, id):
    print("id from path variable: " + id)
    my_product = service.query_product_detail(id)
    print(my_product)
    return JsonResponse({"id": 1, "name": "iphone1", "category": "ELEC"})

@api_view(
    ['GET', 'POST']
)
def comments(request):
    if request.method == 'GET':
        print("geeeeeet")
    else:
        print("poooooooooost")
    return JsonResponse({"code": 200, "message": "Success"})
