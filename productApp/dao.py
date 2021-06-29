#!/usr/bin/env python

from sqlalchemy import create_engine
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
    cursor.execute(
        "select * from product_tab WHERE 1=1 "
        "and name like '%s%' " if name is not None else "%s"
        "and category = '%s' " if category is not None else "%s"      
        "and updated_at > %d "                                                    
        "order by updated_at "
        "limit %d ",
        (name, category, last_updated_at, limit))
    data = cursor.fetchall()
    print(data)
    cursor.close()
    conn.close()

def query_product_detail(id):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from product_tab WHERE id = %s', (id,))
    data = cursor.fetchall()
    print(data)
    cursor.close()
    conn.close()


def data_access():
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3333/db_test?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from USER_tab WHERE id < %s', (55,))
    data = cursor.fetchall()
    print(data)
    cursor.close()
    conn.close()

