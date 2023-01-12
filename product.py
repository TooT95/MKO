
# table name in db
table_name = "product"

# table columns
product_uid = "uid"
product_id = "id"
product_name = "name"
product_created_at = "created_at"
product_is_active = "is_active"

required_fields_to_create = [product_name]

def query_product_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {product_id} LIMIT {(page-1)*limit},{limit}"
def query_product_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {product_id} = {id}"
def query_product_by_uid(id):
    return f"SELECT * FROM {table_name} WHERE {product_uid} = '{id}'"
def query_product_insert(product_object):
    return f"INSERT INTO {table_name} ({product_name},{product_uid},{product_created_at}) VALUES ('{product_object.name}','{product_object.uid}',{product_object.created_at})"

class Product:

    id = 0
    uid = ""
    name = ""
    created_at = 0.0
    is_active = 0

    def __init__(self,id=0,name="",created_at=0.0,uid="",is_active = 0) -> None:
        self.id = id
        self.name = name
        self.created_at = created_at
        self.uid = uid
        self.is_active = is_active

    def toJson(self):
        return {
            product_id:self.id,
            product_name:self.name,
            product_created_at:self.created_at,
            product_uid:self.uid,
            product_is_active:self.is_active,
        }