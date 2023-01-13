import repository
import utils

# table name in db
table_name = "order_product"

# table columns
orderproduct_id = "id"
orderproduct_product_id = "product_id"
orderproduct_price = "price"
orderproduct_count = "count"
orderproduct_sum = "sum"
orderproduct_vat_rate = "vat_rate"
orderproduct_vate_sum = "vate_sum"
orderproduct_total = "total"
orderproduct_order_id = "order_id"
orderproduct_order_by_number = "order_by_number"

required_fields_to_create = [orderproduct_product_id,orderproduct_price,orderproduct_count,orderproduct_sum,orderproduct_vat_rate
    ,orderproduct_vate_sum,orderproduct_total,orderproduct_order_id,orderproduct_order_by_number]
required_fields_to_update = required_fields_to_create.copy().append(orderproduct_id)
required_fields_to_delete = [orderproduct_id,utils.field_action]

def query_orderproduct_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {orderproduct_id} LIMIT {(page-1)*limit},{limit}"
def query_orderproduct_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {orderproduct_id} = {id}"
def query_orderproduct_insert(op_object):
    fields = f'{orderproduct_product_id},{orderproduct_price},{orderproduct_count},{orderproduct_sum},{orderproduct_vat_rate},{orderproduct_vate_sum},{orderproduct_total},{orderproduct_order_id},{orderproduct_order_by_number}'
    values = f'{op_object.product_id},{op_object.price},{op_object.count},{op_object.sum},{op_object.vat_rate},{op_object.vate_sum},{op_object.total},{op_object.order_id},{op_object.order_by_number}'
    return f"INSERT INTO {table_name} ({fields}) VALUES ({values})"
def query_orderproduct_update(op_object):
    fields = f'{orderproduct_product_id} = {op_object.product_id},{orderproduct_price} = {op_object.price},{orderproduct_count} = {op_object.count},{orderproduct_sum} = {op_object.sum},{orderproduct_vat_rate} = {op_object.vat_rate},{orderproduct_vate_sum} = {op_object.vate_sum},{orderproduct_total} = {op_object.total},{orderproduct_order_id} = {op_object.order_id},{orderproduct_order_by_number} = {op_object.order_by_number}'
    return f"UPDATE {table_name} SET {fields} WHERE {orderproduct_id} = {op_object.id}"

class OrderProduct:

    id = 0
    product_id=0
    order_id=0
    price = 0.0
    count = 0.0
    sum = 0.0
    vat_rate = 0
    vate_sum = 0.0
    total = 0.0
    order_by_number = 0
    
    def __init__(self,*args) -> None:
        self.id = args[0]
        self.product_id = args[1]
        self.order_id = args[2]
        self.price = args[3]
        self.count = args[4]
        self.sum = args[5]
        self.vat_rate = args[6]
        self.vate_sum = args[7]
        self.total = args[8]
        self.order_by_number = args[9]
    
    def toJson(self):
        return {
            orderproduct_id:self.id,
            orderproduct_product_id:self.product_id,
            orderproduct_price:self.price,
            orderproduct_count:self.count,
            orderproduct_sum:self.sum,
            orderproduct_vat_rate:self.vat_rate,
            orderproduct_vate_sum:self.vate_sum,
            orderproduct_total:self.total,
            orderproduct_order_id:self.order_id,
            orderproduct_order_by_number:self.order_by_number,
        }