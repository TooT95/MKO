import sqlite3
from utils import *
import product as product_model
import pricetype as pricetype_model
import productprice as productprice_model
import client as client_model
import order as order_model
import orderproduct as orderproduct_model
import paymentschedule as paymentschedule_model

################################################################ -- util -- ################################################################

def delete_element(table_name,id):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(query_delete(table_name,id))
    connection.commit()
    return cursor.lastrowid

def status_change_elem(table_name,id,status):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(query_status_change(table_name,id,status))
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

################################################################ -- client -- ################################################################

def get_client(id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(client_model.query_client_by_id(id))
    client_cursor = cursor.fetchone()
    if client_cursor == None:
        return None
    else:
        pricetype = client_model.Client(*client_cursor)
        return pricetype.toJson()

def get_client_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(client_model.query_client_list(limit,page))
    client_list = []
    for item in cursor.fetchall():
        client = client_model.Client(*item)
        client_list.append(client.toJson())
    return client_list

def update_client(productprice_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(client_model.query_client_update(productprice_object))
    connection.commit()
    return cursor.lastrowid

def create_client(productprice_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(client_model.query_client_insert(productprice_object))
    connection.commit()
    return cursor.lastrowid
################################################################################################################################################

################################################################ -- order -- ################################################################

def get_order(id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(order_model.query_order_by_id(id))
    order_cursor = cursor.fetchone()
    if order_cursor == None:
        return None
    else:
        order = order_model.Order(*order_cursor)
        return order.toJson()

def get_order_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(order_model.query_order_list(limit,page))
    order_list = []
    for item in cursor.fetchall():
        order = order_model.Order(*item)
        order_list.append(order.toJson())
    return order_list

def update_order(order_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(order_model.query_order_update(order_object))
    connection.commit()
    return cursor.lastrowid

def create_order(order_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(order_model.query_order_insert(order_object))
    connection.commit()
    return cursor.lastrowid
################################################################################################################################################

################################################################ -- order product -- ################################################################

def get_orderproduct(id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(orderproduct_model.query_orderproduct_by_id(id))
    orderproduct_cursor = cursor.fetchone()
    if orderproduct_cursor == None:
        return None
    else:
        orderproduct = orderproduct_model.OrderProduct(*orderproduct_cursor)
        return orderproduct.toJson()

def get_orderproduct_by_order_id(order_id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(orderproduct_model.query_orderproduct_by_order_id(order_id))
    orderproduct_list = []
    for item in cursor.fetchall():
        orderproduct = orderproduct_model.OrderProduct(*item)
        orderproduct_list.append(orderproduct.toJson())
    return orderproduct_list

def get_orderproduct_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(orderproduct_model.query_orderproduct_list(limit,page))
    orderproduct_list = []
    for item in cursor.fetchall():
        orderproduct = orderproduct_model.OrderProduct(*item)
        orderproduct_list.append(orderproduct.toJson())
    return orderproduct_list

def update_orderproduct(order_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(orderproduct_model.query_orderproduct_update(order_object))
    connection.commit()
    return cursor.lastrowid

def create_orderproduct(order_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(orderproduct_model.query_orderproduct_insert(order_object))
    connection.commit()
    return cursor.lastrowid
################################################################################################################################################

################################################################ -- payment schedule -- ################################################################

def get_paymentschedule(id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(paymentschedule_model.query_paymentschedule_by_id(id))
    paymentschedule_cursor = cursor.fetchone()
    if paymentschedule_cursor == None:
        return None
    else:
        paymentschedule = paymentschedule_model.PaymentSchedule(*paymentschedule_cursor)
        return paymentschedule.toJson()

def get_paymentschedule_by_order_id(order_id):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(paymentschedule_model.query_paymentschedule_by_order_id(order_id))
    paymentschedule_list = []
    for item in cursor.fetchall():
        paymentschedule = paymentschedule_model.PaymentSchedule(*item)
        paymentschedule_list.append(paymentschedule.toJson())
    return paymentschedule_list

def get_paymentschedule_list(limit,page):
    connection = sqlite3.connect(database_name)
    cursor = connection.execute(paymentschedule_model.query_paymentschedule_list(limit,page))
    paymentschedule_list = []
    for item in cursor.fetchall():
        paymentschedule = paymentschedule_model.PaymentSchedule(*item)
        paymentschedule_list.append(paymentschedule.toJson())
    return paymentschedule_list

def update_paymentschedule(order_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(paymentschedule_model.query_paymentschedule_update(order_object))
    connection.commit()
    return cursor.lastrowid

def create_paymentschedule(order_object):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor = cursor.execute(paymentschedule_model.query_paymentschedule_insert(order_object))
    connection.commit()
    return cursor.lastrowid
################################################################################################################################################
