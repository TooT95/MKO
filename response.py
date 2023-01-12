from flask import Response
import json
import repository 
import product
import productprice
import pricetype
import uuid
import utils
from datetime import datetime

################################################################ -- message and codes -- ################################################################

message_success='OK'
message_code_success = 200

message_not_found_element="not found"
message_code_not_found_element = 101

message_method_not_found ="method not found"
message_code_method_not_found = 404

message_required_fields_empty="Required fields {0} is empty!"
message_code_required_fields_empty = 102

message_error="Error! Text {0}"
message_code_error = 151

################################################################################################################################################

def response_template(message,message_code,result_data=None,additional_fields=None):
    if additional_fields == None:
        additional_fields = {}
    result = {"message":message,"message_code":message_code}
    for item in additional_fields.keys():
        result[item] = additional_fields[item]
    if(result_data!=None):
        result['result'] = result_data
    return Response(json.dumps(result),mimetype='application/json')

def method_not_found():
    return response_template(message_method_not_found,message_code_method_not_found)

################################################################ -- product -- ################################################################

def product_list_response(limit,page):    
    if limit==None:
        limit = 10
    else:
        limit = int(limit)
    if page==None:
        page = 1
    else:
        page = int(page)
    page_limit = {"page":page,"limit":limit}
    return response_template(message_success,message_code_success,repository.get_product_list(limit,page),page_limit)
    
def product_by_id_response(id,is_uid=False):
    if(id==None):
        return response_template(message_not_found_element,message_code_not_found_element,None)    
    result_product = repository.get_product_by_id(id,is_uid)
    if(result_product==None):
        message = message_not_found_element
        message_code = message_code_not_found_element
    else:
        message = message_success
        message_code = message_code_success
    return response_template(message,message_code,result_product)

def product_delete(data):
    required_fields = product.required_fields_to_delete.copy()
    str_data = str(data)
    if(str_data=="b''"):
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    dict_data = json.loads(data)
    for item in product.required_fields_to_delete:
        if item in dict_data:
            required_fields.remove(item)
    if len(required_fields) != 0:
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    
    action = dict_data['action']
    product_object = product.Product()
    product_object.__dict__ = dict_data
    try:
        if(action=='delete'):
            last_id = repository.delete_product(product_object)
            return response_template(message_success,message_code_success,last_id)
        elif(action=='change_status'):
            last_id = repository.status_change_product(product_object,dict_data[utils.field_status])
            return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

def product_update(data):
    required_fields = product.required_fields_to_update.copy()
    str_data = str(data)
    if(str_data=="b''"):
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    dict_data = json.loads(data)
    for item in product.required_fields_to_update:
        if item in dict_data:
            required_fields.remove(item)
    if len(required_fields) != 0:
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    
    product_object = product.Product()
    product_object.__dict__ = dict_data
    try:
        last_id = repository.update_product(product_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

def product_create(data):
    required_fields = product.required_fields_to_create.copy()
    str_data = str(data)
    if(str_data=="b''"):
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    dict_data = json.loads(data)
    for item in product.required_fields_to_create:
        if item in dict_data:
            required_fields.remove(item)
    if len(required_fields) != 0:
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    
    product_object = product.Product()
    dict_data[product.product_uid] = uuid.uuid1()
    dict_data[product.product_created_at] = datetime.now().timestamp()
    product_object.__dict__ = dict_data
    try:
        last_id = repository.create_product(product_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

################################################################################################################################################

################################################################ -- price type -- ################################################################

def pricetype_list_response(limit,page):    
    if limit==None:
        limit = 10
    else:
        limit = int(limit)
    if page==None:
        page = 1
    else:
        page = int(page)
    page_limit = {"page":page,"limit":limit}
    return response_template(message_success,message_code_success,repository.get_pricetype_list(limit,page),page_limit)

def pricetype_create(data):
    required_fields = pricetype.required_fields_to_create.copy()
    str_data = str(data)
    if(str_data=="b''"):
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    dict_data = json.loads(data)
    for item in pricetype.required_fields_to_create:
        if item in dict_data:
            required_fields.remove(item)
    if len(required_fields) != 0:
        print("Hello")
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    
    pricetype_object = pricetype.PriceType()
    dict_data[pricetype.pricetype_uid] = uuid.uuid1()
    dict_data[pricetype.pricetype_created_at] = datetime.now().timestamp()
    pricetype_object.__dict__ = dict_data
    try:
        last_id = repository.create_pricetype(pricetype_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

def pricetype_by_id_response(id,is_uid=False):
    if(id==None):
        return response_template(message_not_found_element,message_code_not_found_element,None)    
    result_product = repository.get_pricetype_by_id(id,is_uid)
    if(result_product==None):
        message = message_not_found_element
        message_code = message_code_not_found_element
    else:
        message = message_success
        message_code = message_code_success
    return response_template(message,message_code,result_product)

################################################################################################################################################

################################################################ -- price type -- ################################################################

def product_price(id,by_pricetype=True):
    if(id==None):
        return response_template(message_not_found_element,message_code_not_found_element,None)    
    result_price = repository.get_product_price(id,by_pricetype)
    if(result_price==None):
        message = message_not_found_element
        message_code = message_code_not_found_element
    else:
        message = message_success
        message_code = message_code_success
    return response_template(message,message_code,result_price)

def product_price_list(limit,page):
    if limit==None:
        limit = 10
    else:
        limit = int(limit)
    if page==None:
        page = 1
    else:
        page = int(page)
    page_limit = {"page":page,"limit":limit}
    return response_template(message_success,message_code_success,repository.get_product_price_list(limit,page),page_limit)

def product_price_create(data):
    required_fields = productprice.required_fields_to_create.copy()
    str_data = str(data)
    if(str_data=="b''"):
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    dict_data = json.loads(data)
    for item in productprice.required_fields_to_create:
        if item in dict_data:
            required_fields.remove(item)
    if len(required_fields) != 0:
        print("Hello")
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    
    productprice_object = productprice.ProductPrice()
    dict_data[product.table_name] = repository.get_product_by_id(dict_data[productprice.product_price_product_id],False)
    dict_data[pricetype.table_name] = repository.get_pricetype_by_id(dict_data[productprice.product_price_price_type_id],False)
    dict_data[productprice.product_price_created_at] = datetime.now().timestamp()
    productprice_object.__dict__ = dict_data
    try:
        last_id = repository.query_productprice_insert(productprice_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)
################################################################################################################################################

# with open("price_type.txt", encoding="utf8") as file:
#     jsondata = json.loads(file.read())
#     for item in jsondata['result']:
#         dict_data = {}
#         dict_data['name'] = item['ВидЦены']
#         pricetype_object = pricetype.PriceType()
#         dict_data[pricetype.pricetype_uid] = item['УникальныйИдентификатор']
#         dict_data[pricetype.pricetype_created_at] = datetime.now().timestamp()
#         pricetype_object.__dict__ = dict_data
#         lastid = repository.create_pricetype(pricetype_object)
#         print(lastid)
    
