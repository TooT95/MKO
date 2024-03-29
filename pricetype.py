
import utils

# table name in db
table_name = "price_type"

# table columns
pricetype_id = "id"
pricetype_name = "name"
pricetype_created_at = "created_at"
pricetype_is_active = "is_active"

required_fields_to_create = [pricetype_name]
required_fields_to_update = [pricetype_id,pricetype_name]
required_fields_to_delete = [pricetype_id,utils.field_action]

def query_pricetype_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {pricetype_id} LIMIT {(page-1)*limit},{limit}"
def query_pricetype_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {pricetype_id} = {id}"
def query_pricetype_insert(pricetype_object):
    return f"INSERT INTO {table_name} ({pricetype_name},{pricetype_created_at}) VALUES ('{pricetype_object.name}',{pricetype_object.created_at})"
def query_pricetype_update(pricetype_object):
    return f"UPDATE {table_name} SET {pricetype_name} = '{pricetype_object.name}' WHERE {pricetype_id} = {pricetype_object.id}"

class PriceType:

    id = 0
    name = ""
    created_at = 0.0
    is_active = 0

    def __init__(self,id=0,name="",created_at=0.0,is_active = 0) -> None:
        self.id = id
        self.name = name
        self.created_at = created_at
        self.is_active = is_active

    def toJson(self):
        return {
            pricetype_id:self.id,
            pricetype_name:self.name,
            pricetype_created_at:self.created_at,
            pricetype_is_active:self.is_active,
        }