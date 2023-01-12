import sqlite3
from utils import *
import product as product_model
import pricetype as pricetype_model
import productprice as productprice_model


################################################################ -- util -- ################################################################

def delete_element(table_name,id):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(query_delete(table_name,id))
    connection.commit()
    return cursor.lastrowid

def status_change_elem(id,status):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(query_status_change(product_model.table_name,id,status))
    connection.commit()
    return cursor.lastrowid

################################################################################################################################################

################################################################ -- price type -- ################################################################

def get_product_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(product_model.query_product_list(limit,page))
    product_list = []
    for item in cursor.fetchall():
        product = product_model.Product(*item)
        product_list.append(product.toJson())
    return product_list

def get_product_by_id(id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(product_model.query_product_by_id(id))
    product_cursor = cursor.fetchone()
    if product_cursor == None:
        return None
    else:
        product = product_model.Product(*product_cursor)
        return product.toJson()

def update_product(product_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(product_model.query_product_update(product_object))
    connection.commit()
    return cursor.lastrowid

def create_product(product_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(product_model.query_product_insert(product_object))
    connection.commit()
    return cursor.lastrowid

################################################################################################################################################

################################################################ -- price type -- ################################################################

def get_pricetype_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(pricetype_model.query_pricetype_list(limit,page))
    product_list = []
    for item in cursor.fetchall():
        product = pricetype_model.PriceType(*item)
        product_list.append(product.toJson())
    return product_list

def delete_pricetype(pricetype_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(query_delete(pricetype_model.table_name,pricetype_object.id))
    connection.commit()
    return cursor.lastrowid

def status_change_pricetype(pricetype_object,status):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(query_status_change(pricetype_model.table_name,pricetype_object.id,status))
    connection.commit()
    return cursor.lastrowid

def update_pricetype(pricetype_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(pricetype_model.query_pricetype_update(pricetype_object))
    connection.commit()
    return cursor.lastrowid

def create_pricetype(pricetype_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(pricetype_model.query_pricetype_insert(pricetype_object))
    connection.commit()
    return cursor.lastrowid

def get_pricetype_by_id(id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(pricetype_model.query_pricetype_by_id(id))
    pricetype_cursor = cursor.fetchone()
    if pricetype_cursor == None:
        return None
    else:
        pricetype = pricetype_model.PriceType(*pricetype_cursor)
        return pricetype.toJson()

################################################################################################################################################

################################################################ -- product price -- ################################################################

def get_product_price(id,by_price_type):
    connection = sqlite3.connect(database_name)
    if(by_price_type):
        cursor = connection.execute(productprice_model.query_product_price_pricetype(id))
    else:
        cursor = connection.execute(productprice_model.query_product_price_product(id))
    productprice_cursor = cursor.fetchall()
    productprice_list = []
    for cursor_item in productprice_cursor:
        pricetype = productprice_model.ProductPrice(*cursor_item)
        productprice_list.append(pricetype.toJson())
    return productprice_list

def get_product_price_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(productprice_model.query_product_price_list(limit,page))
    product_list = []
    for item in cursor.fetchall():
        product = productprice_model.ProductPrice(*item)
        product_list.append(product.toJson())
    return product_list

def query_productprice_update(productprice_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(productprice_model.query_product_price_update(productprice_object))
    connection.commit()
    return cursor.lastrowid

def query_productprice_insert(productprice_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(productprice_model.query_product_price_insert(productprice_object))
    connection.commit()
    return cursor.lastrowid
################################################################################################################################################