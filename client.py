
import utils

# table name in db
table_name = "client"

# table columns
client_id = "id"
client_name = "name"
client_inn = "inn"
client_created_at = "created_at"
client_is_active = "is_active"

required_fields_to_create = [client_name,client_inn]
required_fields_to_update = [client_id,client_name,client_inn]
required_fields_to_delete = [client_id,utils.field_action]

def query_client_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {client_id} LIMIT {(page-1)*limit},{limit}"
def query_client_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {client_id} = {id}"
def query_client_insert(client_object):
    return f"INSERT INTO {table_name} ({client_name},{client_inn},{client_created_at}) VALUES ('{client_object.name}','{client_object.inn}',{client_object.created_at})"
def query_client_update(client_object):
    return f"UPDATE {table_name} SET {client_name} = '{client_object.name}',{client_inn} = '{client_object.inn}' WHERE {client_id} = {client_object.id}"

class Client:

    id = 0
    name = ""
    inn = ""
    created_at = 0.0
    is_active = 0

    def __init__(self,id=0,name="",inn="",created_at=0.0,is_active = 0) -> None:
        self.id = id
        self.name = name
        self.inn = inn
        self.created_at = created_at
        self.is_active = is_active

    def toJson(self):
        return {
            client_id:self.id,
            client_name:self.name,
            client_inn:self.inn,
            client_created_at:self.created_at,
            client_is_active:self.is_active,
        }