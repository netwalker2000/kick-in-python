import time

from django.http import JsonResponse

from user import register, login

cache = {}

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
    data = register.register_user(name, password, email)
    print(str(data))
    register_payload = {
        "code": 200,
        "message": "Success",
    }
    return JsonResponse(register_payload)


def user_login(request):
    name = "user"
    if "name" in request.GET.keys():
        name = request.GET["name"]

    if name in cache.keys():
        data = cache[name]
        # print("cached")
    else:
        password = "password"
        if "password" in request.GET.keys():
            password = request.GET["password"]
        data = login.user_login(name, password)
        cache[name] = data
        # print("not cached, set cache")

    # todo: format data
    login_payload = {
        "code": 200,
        "message": "Success",
        "token": data
    }
    return JsonResponse(login_payload)
