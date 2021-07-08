import functools
import logging
import time

from django.http import JsonResponse

from user import register, login


def param_pre_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('call %s' % func.__name__)
        logging.info('args = {}'.format(*args))
        request = args[0]
        err_payload = {
            "code": 400,
            "message": "parameters invalid!"
        }
        if "name" not in request.GET.keys():
            logging.warn("name not exist in request!")
            return JsonResponse(err_payload)
        if "password" not in request.GET.keys():
            logging.warn("password not exist in request!")
            return JsonResponse(err_payload)
        return func(*args, **kwargs)
    return wrapper


@param_pre_check
def user_register(request):
    name = request.GET["name"]
    password = request.GET["password"]
    email = request.GET["email"]
    logging.info("variables:[%s] [%s] [%s] " % (name, password, email))
    data = register.register_user(name, password, email)
    logging.info(str(data))
    register_payload = {
        "code": 200,
        "message": "Success",
    }
    return JsonResponse(register_payload)


@param_pre_check
def user_login(request):
    name = request.GET["name"]
    password = request.GET["password"]

    data = login.user_login(name, password)

    # todo: format data
    login_payload = {
        "code": 200,
        "message": "Success",
        "token": data
    }
    return JsonResponse(login_payload)
