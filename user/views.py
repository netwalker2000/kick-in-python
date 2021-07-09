import functools
import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import utils.checks
from user import register, login


@csrf_exempt
@utils.checks.method_param_check_request("POST", "name", "password", "email")
def user_register(request):
    r_dict = json.loads(request.body)
    name = r_dict["name"]
    password = r_dict["password"]
    email = r_dict["email"]
    is_correct = utils.checks.check_email(email)
    if not is_correct:
        err_msg = "Invalid Email {}".format(email)
        err_payload = {
            "code": 400,
            "message": err_msg
        }
        return JsonResponse(err_payload)
    data = register.register_user(name, password, email)
    logging.info(str(data))
    register_payload = {
        "code": 200,
        "message": "Success",
    }
    return JsonResponse(register_payload)


@csrf_exempt
@utils.checks.method_param_check_request("POST", "name", "password")
def user_login(request):
    r_dict = json.loads(request.body)
    name = r_dict["name"]
    password = r_dict["password"]
    token = login.user_login(name, password)
    if token != "None":
        return JsonResponse({
            "code": 200,
            "message": "Success",
            "token": token
        })
    else:
        return JsonResponse({
            "code": 400,
            "message": "Can not login, unmatched!"
        })

