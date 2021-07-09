# Python program to validate an Email
import functools
import json
import logging
import re

# Make a regular expression
# for validating an Email
from django.http import JsonResponse

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Define a function for
# for validating an Email


def check_email(email):
    # pass the regular expression
    # and the string in search() method
    if re.match(regex, email) is not None:
        return True
    else:
        return False


def method_param_check_request(*inputs):
    def param_pre_check(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            if inputs[0] == "GET":
                keys = request.GET.keys()
            else:
                keys = json.loads(request.body).keys()
            for idx, element in enumerate(inputs):
                if idx == 0:
                    continue
                else:
                    if element not in keys:
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

