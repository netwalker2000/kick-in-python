import functools
import logging

from django.http import JsonResponse
from django.core.cache import cache

import utils.checks
from productProject import settings
from user import register, login


def param_exist_in_request(*inputs):
    def param_pre_check(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            for _, element in enumerate(inputs):
                if element not in request.GET.keys():
                    err_msg = "{} does not exist in request!".format(element)
                    logging.warn(err_msg)
                    err_payload = {
                        "code": 400,
                        "message": err_msg
                    }
                    return JsonResponse(err_payload)
            return func(*args, **kwargs)

        return wrapper

    return param_pre_check


@param_exist_in_request("name", "password", "email")
def user_register(request):
    # if httpmethod == post
    name = request.GET["name"]
    password = request.GET["password"]
    email = request.GET["email"]
    is_correct, err_payload = utils.checks.check_email(email)
    if not is_correct:
        return JsonResponse(err_payload)
    logging.info("variables:[%s] [%s] [%s] " % (name, password, email))
    data = register.register_user(name, password, email)
    logging.info(str(data))
    register_payload = {
        "code": 200,
        "message": "Success",
    }
    return JsonResponse(register_payload)


@param_exist_in_request("name", "password")
def user_login(request):
    name = request.GET["name"]
    password = request.GET["password"]
    try:
        cached_pw = cache.get("name_key_%s" % name)
    except:
        pass
    if cached_pw != "" and password == cached_pw:
        token = cached_pw  # todo: hashed the pw ,and also store token
    else:
        token = login.user_login(name, password)
        # cache.set("name_key_%s" % name, password, settings.CACHE_TIMEOUT)

    # todo: format data
    login_payload = {
        "code": 200,
        "message": "Success",
        "token": token
    }
    return JsonResponse(login_payload)
