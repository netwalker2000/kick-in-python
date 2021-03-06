import time

import models


def query_comments(product_id):
    data = models.CommentTab.objects.filter(topic_id=product_id)
    return data


def create_comment(product_id, content, user_id, user_name):
    models.CommentTab.objects.create(
        topic_id=product_id,
        content=content,
        user_id=user_id,
        user_name=user_name,
        status=0,
        created_at=int(time.time()),
        updated_at=int(time.time())
    )
    return True
