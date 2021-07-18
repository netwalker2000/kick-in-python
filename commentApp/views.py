# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import time

from django.http import JsonResponse
import service
import user


# global storage for comments tree to save the resource
import utils.checks
from commentApp.serializers import CommentSerializer
from user.login import login_validate_decorator

global_comment_cache = {}


@login_validate_decorator
def comments(request, id):
    # return cached if not expired
    if id in global_comment_cache:
        logging.info("hit cache!")
        logging.info(global_comment_cache[id])
        # return global_comment_cache[id].comment_payload
    data = service.query_comments(id)
    model_map = {}
    for model in data:
        model_map[model.id] = model

    comment_payload = {
        "code": 200,
        "message": "Success",
        "comments": [CommentSerializer().convert_to_dict(comment, model_map) for comment in data]
    }
    logging.info(comment_payload)
    if id not in global_comment_cache:
        global_comment_cache[id] = {
            "id": id,
            "created_at": time.time(),
            "expired_at": time.time(),
            "comment_payload": comment_payload
        }
    return JsonResponse(comment_payload)


@login_validate_decorator
@utils.checks.method_param_check_request("POST", "content", "user_id", "user_name")
def create_comment(request, id):
    logging.info("id from path variable: " + id)
    r_dict = json.loads(request.body)
    content = r_dict["content"]
    user_id = r_dict["user_id"]
    user_name = r_dict["user_name"]
    service.create_comment(id, content, user_id, user_name)
    return JsonResponse({"code": 200, "message": "Success"})
