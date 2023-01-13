from datetime import datetime
import uuid 

# print(datetime.now().timestamp())
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

orderP = OrderProduct(1,2,3,4,5,6,7,8,9,10)
print(orderP.__getattribute__('order_by_number'))
