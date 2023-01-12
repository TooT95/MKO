import repository
import utils

# table name in db
table_name = "_order"

# table columns
order_id = "id"
order_date = "date"
order_client_id = "client_id"
order_status = "status"
order_created_at = "created_at"
order_is_active = "is_active"

required_fields_to_create = [order_date,order_client_id,order_status]
required_fields_to_update = [order_id,order_date,order_client_id,order_status]
required_fields_to_delete = [order_id,utils.field_action]

def query_order_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {order_id} LIMIT {(page-1)*limit},{limit}"
def query_order_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {order_id} = {id}"
def query_order_insert(order_object):
    return f"INSERT INTO {table_name} ({order_date},{order_client_id},{order_created_at}) VALUES ('{order_object.name}','{order_object.inn}',{order_object.created_at})"
def query_order_update(order_object):
    return f"UPDATE {table_name} SET {order_date} = '{order_object.name}',{order_client_id} = '{order_object.inn}' WHERE {order_id} = {order_object.id}"

class Order:

    id = 0
    date=0.0
    client_id=0
    created_at = 0.0
    is_active = 0
    status=""

    def __init__(self,id=0,date=0.0,client_id=0,created_at=0.0,is_active = 0,status="") -> None:
        self.id = id
        self.date = date
        self.client_id = client_id
        self.created_at = created_at
        self.is_active = is_active
        self.status = status

    def toJson(self):
        return {
            order_id:self.id,
            order_date:self.date,
            order_client_id:repository.get_client(self.client_id),
            order_created_at:self.created_at,
            order_is_active:self.is_active,
            order_status:self.status
        }