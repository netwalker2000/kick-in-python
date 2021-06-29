import models
import dao


def product_service(name, category, last_updated_at, limit):
    print("inner params [%s || %s || %d || %d]" % (name, category, last_updated_at, limit))
    data = dao.query_product_list(name, category, last_updated_at, limit)
    return data


def query_product_detail(product_id):
    data = models.ProductTab.objects.filter(id=product_id)
    print(data)
    return data
