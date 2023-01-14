
database_name = "mko.db"

_product = 0
_pricetype = 1
_productprice = 2
_client = 3
_order = 4
_orderproduct = 5
_paymentschedule = 6

field_action = "action"
field_status = "status"
field_is_active = "is_active"
field_id = "id"

def query_status_change(table_name,id,status):
    return f"UPDATE {table_name} SET {field_is_active} = {status} WHERE {field_id} = {id}"
def query_delete(table_name,id):
    return f"DELETE FROM {table_name} WHERE {field_id} = {id}"
