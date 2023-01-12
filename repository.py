import sqlite3
from utils import *
import product as product_model
import pricetype as pricetype_model
import productprice as productprice_model

################################################################ -- price type -- ################################################################

def get_product_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(product_model.query_product_list(limit,page))
    product_list = []
    for item in cursor.fetchall():
        product = product_model.Product(*item)
        product_list.append(product.toJson())
    return product_list

def get_product_by_id(id,is_uid):
    connection = sqlite3.connect(database_name)
    if(is_uid):
        cursor = connection.execute(product_model.query_product_by_uid(id))
    else:
        cursor = connection.execute(product_model.query_product_by_id(id))
    product_cursor = cursor.fetchone()
    if product_cursor == None:
        return None
    else:
        product = product_model.Product(*product_cursor)
        return product.toJson()

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

def create_pricetype(product_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(pricetype_model.query_pricetype_insert(product_object))
    connection.commit()
    return cursor.lastrowid

def get_pricetype_by_id(id,is_uid):
    connection = sqlite3.connect(database_name)
    if(is_uid):
        cursor = connection.execute(pricetype_model.query_pricetype_by_uid(id))
    else:
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
        # cursor = connection.execute(pricetype_model.query_pricetype_by_uid(id))
        return None
    else:
        cursor = connection.execute(productprice_model.query_product_price_pricetype(id))
    productprice_cursor = cursor.fetchone()
    if productprice_cursor == None:
        return None
    else:
        pricetype = productprice_model.ProductPrice(*productprice_cursor)
        return pricetype.toJson()

################################################################################################################################################