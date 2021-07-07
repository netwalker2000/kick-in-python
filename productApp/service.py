import logging

import models


def product_service(name, category, last_updated_at, limit):
    logging.info("inner params [%s || %s || %d || %d]" % (name, category, last_updated_at, limit))
    objs = models.ProductTab.objects
    if name:
        objs = objs.filter(name=name)
    if category:
        objs = objs.filter(category=category)
    objs = objs.exclude(updated_at__lt=last_updated_at)
    data = objs.order_by("updated_at")
    # layer
    logging.info(data)
    return data


def query_product_detail(product_id):
    data = models.ProductTab.objects.filter(id=product_id)
    logging.info(data)
    return data


def query_photos(product_id):
    data = models.PhotoTab.objects.filter(product_id=product_id)
    return data
