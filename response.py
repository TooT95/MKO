from flask import Response
import json
import repository 
import product,productprice,pricetype,client,order,orderproduct
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

################################################################ -- common, enum -- ################################################################

def response_template(message,message_code,result_data=None,additional_fields=None):
    if additional_fields == None:
        additional_fields = {}
    result = {"message":message,"message_code":message_code}
    for item in additional_fields.keys():
        result[item] = additional_fields[item]
    if(result_data!=None):
        result['result'] = result_data
    return Response(json.dumps(result),mimetype='application/json')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def method_not_found():
    return response_template(message_method_not_found,message_code_method_not_found)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def check_field_to_empty(data,_required_fields):
    required_fields = _required_fields.copy()
    str_data = str(data)
    if(str_data=="b''"):
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    dict_data = json.loads(data)
    for item in _required_fields:
        if item in dict_data:
            required_fields.remove(item)
    if len(required_fields) != 0:
        return response_template(message_required_fields_empty.format(','.join(required_fields)),message_code_required_fields_empty)
    return None

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def find_elem_delete(dict_data,table_name):
    action = dict_data['action']
    id = dict_data[utils.field_id]
    try:
        if(action=='delete'):
            last_id = repository.delete_element(table_name,id)
            return response_template(message_success,message_code_success,last_id)
        elif(action=='change_status'):
            status = dict_data[utils.field_status]
            last_id = repository.status_change_elem(table_name,id,status)
            return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def get_list_response(object_type,limit,page):
    if limit==None:
        limit = 10
    else:
        limit = int(limit)
    if page==None:
        page = 1
    else:
        page = int(page)
    page_limit = {"page":page,"limit":limit}
    if(object_type == utils._product):
        result = repository.get_product_list(limit,page)
    elif(object_type == utils._pricetype):
        result = repository.get_pricetype_list(limit,page)
    elif(object_type == utils._productprice):
        result = repository.get_product_price_list(limit,page)
    elif(object_type == utils._client):
        result = repository.get_client_list(limit,page)
    elif(object_type == utils._order):
        result = repository.get_order_list(limit,page)
    elif(object_type == utils._orderproduct):
        result = repository.get_orderproduct_list(limit,page)
    else:
        return response_template(message_method_not_found,message_code_method_not_found)
    return response_template(message_success,message_code_success,result,page_limit)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def get_by_id(object_type,id,by_pricetype=False):
    if(id==None):
        return response_template(message_not_found_element,message_code_not_found_element,None)    
    if(object_type == utils._product):
        _result = repository.get_product_by_id(id)
    elif(object_type == utils._pricetype):
        _result = repository.get_pricetype_by_id(id)
    elif(object_type == utils._productprice):
        _result = repository.get_product_price(id,by_pricetype)
    elif(object_type == utils._client):
        _result = repository.get_client(id)
    elif(object_type == utils._order):
        _result = repository.get_order(id)
    elif(object_type == utils._order):
        _result = repository.get_orderproduct(id)
    else:
        return response_template(message_method_not_found,message_code_method_not_found)
    
    if(_result==None):
        message = message_not_found_element
        message_code = message_code_not_found_element
    else:
        message = message_success
        message_code = message_code_success
    return response_template(message,message_code,_result)

################################################################ -- product -- ################################################################

def product_list_response(limit,page):    
    return get_list_response(utils._product,limit,page)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_by_id_response(id):
    return get_by_id(utils._product,id)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_delete(data):
    check_result = check_field_to_empty(data,product.required_fields_to_delete)
    if check_result != None:
        return check_result

    dict_data = json.loads(data)
    return find_elem_delete(dict_data,product.table_name)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_update(data):
    check_result = check_field_to_empty(data,product.required_fields_to_update)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    product_object = product.Product()
    product_object.__dict__ = dict_data
    try:
        last_id = repository.update_product(product_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_create(data):
    check_result = check_field_to_empty(data,product.required_fields_to_create)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    product_object = product.Product()
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
    return get_list_response(utils._pricetype,limit,page)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def pricetype_by_id_response(id):
    return get_by_id(utils._pricetype,id)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def pricetype_delete(data):
    check_result = check_field_to_empty(data,pricetype.required_fields_to_delete)
    if check_result != None:
        return check_result

    dict_data = json.loads(data)
    return find_elem_delete(dict_data,pricetype.table_name)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def pricetype_update(data):
    check_result = check_field_to_empty(data,pricetype.required_fields_to_update)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    pricetype_object = pricetype.PriceType()
    pricetype_object.__dict__ = dict_data
    try:
        last_id = repository.update_pricetype(pricetype_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def pricetype_create(data):
    check_result = check_field_to_empty(data,pricetype.required_fields_to_create)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    pricetype_object = pricetype.PriceType()
    dict_data[pricetype.pricetype_created_at] = datetime.now().timestamp()
    pricetype_object.__dict__ = dict_data
    try:
        last_id = repository.create_pricetype(pricetype_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

################################################################################################################################################

################################################################ -- product price -- ################################################################

def product_price(id,by_pricetype=True):
    return get_by_id(utils._productprice,id,by_pricetype)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_price_list(limit,page):    
    return get_list_response(utils._productprice,limit,page)

def product_price_delete(data):
    check_result = check_field_to_empty(data,productprice.required_fields_to_delete)
    if check_result != None:
        return check_result

    dict_data = json.loads(data)
    return find_elem_delete(dict_data,productprice.table_name)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_price_update(data):
    check_result = check_field_to_empty(data,productprice.required_fields_to_update)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    productprice_object = productprice.ProductPrice()
    dict_data[product.table_name] = repository.get_product_by_id(dict_data[productprice.product_price_product_id])
    dict_data[pricetype.table_name] = repository.get_pricetype_by_id(dict_data[productprice.product_price_price_type_id])
    productprice_object.__dict__ = dict_data
    try:
        last_id = repository.query_productprice_update(productprice_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def product_price_create(data):
    check_result = check_field_to_empty(data,productprice.required_fields_to_create)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    productprice_object = productprice.ProductPrice()
    dict_data[product.table_name] = repository.get_product_by_id(dict_data[productprice.product_price_product_id])
    dict_data[pricetype.table_name] = repository.get_pricetype_by_id(dict_data[productprice.product_price_price_type_id])
    dict_data[productprice.product_price_created_at] = datetime.now().timestamp()
    productprice_object.__dict__ = dict_data
    try:
        last_id = repository.query_productprice_insert(productprice_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)
################################################################################################################################################


################################################################ -- client -- ################################################################

def client_list_response(limit,page):    
    return get_list_response(utils._client,limit,page)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def client_by_id_response(id):
    return get_by_id(utils._client,id)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def client_delete(data):
    check_result = check_field_to_empty(data,client.required_fields_to_delete)
    if check_result != None:
        return check_result

    dict_data = json.loads(data)
    return find_elem_delete(dict_data,client.table_name)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def client_update(data):
    check_result = check_field_to_empty(data,client.required_fields_to_update)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    client_object = client.Client()
    client_object.__dict__ = dict_data
    try:
        last_id = repository.update_client(client_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def client_create(data):
    check_result = check_field_to_empty(data,client.required_fields_to_create)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    product_object = client.Client()
    dict_data[client.client_created_at] = datetime.now().timestamp()
    product_object.__dict__ = dict_data
    try:
        last_id = repository.create_client(product_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

################################################################################################################################################

################################################################ -- order -- ################################################################

def order_list_response(limit,page):    
    return get_list_response(utils._order,limit,page)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def order_by_id_response(id):
    return get_by_id(utils._order,id)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def order_delete(data):
    check_result = check_field_to_empty(data,order.required_fields_to_delete)
    if check_result != None:
        return check_result

    dict_data = json.loads(data)
    return find_elem_delete(dict_data,order.table_name)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def order_update(data):
    check_result = check_field_to_empty(data,order.required_fields_to_update)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    order_object = order.Order()
    order_object.__dict__ = dict_data
    try:
        last_id = repository.update_order(order_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def order_create(data):
    check_result = check_field_to_empty(data,order.required_fields_to_create)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    order_object = order.Order()
    dict_data[order.order_created_at] = datetime.now().timestamp()
    order_object.__dict__ = dict_data
    try:
        last_id = repository.create_order(order_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

################################################################################################################################################

################################################################ -- order product -- ################################################################

def orderproduct_list_response(limit,page):    
    return get_list_response(utils._orderproduct,limit,page)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def orderproduct_by_id_response(id):
    return get_by_id(utils._orderproduct,id)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def orderproduct_delete(data):
    check_result = check_field_to_empty(data,orderproduct.required_fields_to_delete)
    if check_result != None:
        return check_result

    dict_data = json.loads(data)
    return find_elem_delete(dict_data,orderproduct.table_name)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def orderproduct_update(data):
    check_result = check_field_to_empty(data,orderproduct.required_fields_to_update)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    orderproduct_object = orderproduct.OrderProduct()
    orderproduct_object.__dict__ = dict_data
    try:
        last_id = repository.update_orderproduct(orderproduct_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def orderproduct_create(data):
    check_result = check_field_to_empty(data,orderproduct.required_fields_to_create)
    if check_result != None:
        return check_result
    
    dict_data = json.loads(data)
    orderproduct_object = orderproduct.OrderProduct()
    dict_data[orderproduct.order_created_at] = datetime.now().timestamp()
    orderproduct_object.__dict__ = dict_data
    try:
        last_id = repository.create_orderproduct(orderproduct_object)
        return response_template(message_success,message_code_success,last_id)
    except Exception as ex:
        return response_template(message_error.format(str(ex)),message_code_error)

################################################################################################################################################
