import dao

def product_service():
    dao.data_access()

def query_product_detail(id):
    return dao.query_product_detai(id)