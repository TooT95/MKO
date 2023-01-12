
# table name in db
table_name = "price_type"

# table columns
pricetype_uid = "uid"
pricetype_id = "id"
pricetype_name = "name"
pricetype_created_at = "created_at"
pricetype_is_active = "is_active"

required_fields_to_create = [pricetype_name]

def query_pricetype_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {pricetype_id} LIMIT {(page-1)*limit},{limit}"
def query_pricetype_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {pricetype_id} = {id}"
def query_pricetype_by_uid(id):
    return f"SELECT * FROM {table_name} WHERE {pricetype_uid} = '{id}'"
def query_pricetype_insert(pricetype_object):
    return f"INSERT INTO {table_name} ({pricetype_name},{pricetype_uid},{pricetype_created_at}) VALUES ('{pricetype_object.name}','{pricetype_object.uid}',{pricetype_object.created_at})"

class PriceType:

    id = 0
    uid = ""
    name = ""
    created_at = 0.0
    is_active = 0

    def __init__(self,id=0,name="",uid="",created_at=0.0,is_active = 0) -> None:
        self.id = id
        self.name = name
        self.created_at = created_at
        self.uid = uid
        self.is_active = is_active

    def toJson(self):
        return {
            pricetype_id:self.id,
            pricetype_name:self.name,
            pricetype_created_at:self.created_at,
            pricetype_uid:self.uid,
            pricetype_is_active:self.is_active,
        }