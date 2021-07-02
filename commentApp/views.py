# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from django.http import JsonResponse
import service
import user


# global storage for comments tree to save the resource
from commentApp.serializers import CommentSerializer

global_comment_cache = {}


# Create your views here.
def comments(request, id):
    # todo: use meta program @validation
    name = "user"
    if "name" in request.GET.keys():
        name = request.GET["name"]
    apply_timestamp = "1625213873"
    if "apply_timestamp" in request.GET.keys():
        apply_timestamp = request.GET["apply_timestamp"]
    token = ""
    if "token" in request.GET.keys():
        token = request.GET["token"]
    if not user.login.validate_token(name, apply_timestamp, token):
        return JsonResponse({"code": 403, "message": "Invalid token"})

    print("id from path variable: " + id)
    if request.method == 'GET':
        # return cached if not expired
        if id in global_comment_cache:
            print("hit cache!")
            print(global_comment_cache[id])
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
        print(comment_payload)
        if id not in global_comment_cache:
            global_comment_cache[id] = {
                "id": id,
                "created_at": time.time(),
                "expired_at": time.time(), # add 60 sec
                "comment_payload": comment_payload
            }
        return JsonResponse(comment_payload)
    else:
        service.create_comment(1, "This is the comment", 1, "user_name")
        return JsonResponse({"code": 200, "message": "Success"})
