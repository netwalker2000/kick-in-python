#!/usr/bin/env python
import json
from time import strftime

from sqlalchemy import create_engine

import models

print("Begin...")

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3333/product_db?charset=utf8",
    max_overflow=0,
    pool_size=5,
    pool_timeout=30,
    pool_recycle=-1
)


def query_product_list(name, category, last_updated_at, limit):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    where_name = "and name like '" + name + "%' " if name else ""
    where_category = "and category like '" + category + "%' " if category else ""
    sql = "select * from product_tab WHERE 1=1 " + where_name + where_category + " and updated_at > " + str(
        last_updated_at) + " order by updated_at limit " + str(limit)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    conn.close()
    return data

