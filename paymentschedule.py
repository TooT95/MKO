import repository
import utils

# table name in db
table_name = "payment_schedule"

# table columns
paymentschedule_id = "id"
paymentschedule_order_id = "order_id"
paymentschedule_payment_type = "payment_type"
paymentschedule_payment_date = "payment_date"
paymentschedule_sum = "sum"

required_fields_to_create = [paymentschedule_order_id,paymentschedule_payment_type,paymentschedule_payment_date]
required_fields_to_update = [paymentschedule_id,paymentschedule_order_id,paymentschedule_payment_type,paymentschedule_payment_date]
required_fields_to_delete = [paymentschedule_id,utils.field_action]

def query_paymentschedule_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {paymentschedule_id} LIMIT {(page-1)*limit},{limit}"
def query_paymentschedule_by_id(id):
    return f"SELECT * FROM {table_name} WHERE {paymentschedule_id} = {id}"
def query_paymentschedule_by_order_id(order_id):
    return f"SELECT * FROM {table_name} WHERE {paymentschedule_order_id} = {order_id}"
def query_paymentschedule_insert(psch_object):
    return f"INSERT INTO {table_name} ({paymentschedule_order_id},{paymentschedule_payment_type},{paymentschedule_payment_date},{paymentschedule_sum}) VALUES ({psch_object.order_id},'{psch_object.payment_type}',{psch_object.payment_date},{psch_object.sum})"
def query_paymentschedule_update(psch_object):
    return f"UPDATE {table_name} SET {paymentschedule_order_id} = {psch_object.order_id},{paymentschedule_payment_type} = '{psch_object.payment_type}',{paymentschedule_payment_date} = {psch_object.payment_date},{paymentschedule_sum} = {psch_object.sum} WHERE {paymentschedule_id} = {psch_object.id}"

class PaymentSchedule:

    id = 0
    order_id=0
    payment_type=""
    payment_date = 0.0
    sum = 0.0
    
    def __init__(self,id = 0,order_id=0,payment_type="",payment_date = 0.0,sum = 0.0) -> None:
        self.id = id
        self.order_id = order_id
        self.payment_type = payment_type
        self.payment_date = payment_date
        self.sum = sum

    def toJson(self):
        return {
            paymentschedule_id:self.id,
            paymentschedule_order_id:self.order_id,
            paymentschedule_payment_type:self.payment_type,
            paymentschedule_payment_date:self.payment_date,
            paymentschedule_sum:self.sum
        }