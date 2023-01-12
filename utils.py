
database_name = "mko.db"

field_action = "action"
field_status = "status"
field_is_active = "is_active"
field_id = "id"

def query_status_change(table_name,id,status):
    return f"UPDATE {table_name} SET {field_is_active} = {status} WHERE {field_id} = {id}"
def query_delete(table_name,id):
    return f"DELETE FROM {table_name} WHERE {field_id} = {id}"
