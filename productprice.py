
# table name in db
table_name = "product_price"

# table columns
product_price_id = "id"
product_price_product_id = "product_id"
product_price_price = "price"
product_price_created_at = "created_at"
product_price_price_type_id = "price_type_id"

def query_product_price_pricetype(id):
    return f"SELECT * FROM {table_name} WHERE {product_price_price_type_id}={id}"

class ProductPrice:

    id = 0
    product_id = 0
    price = 0.0
    price_type_id = 0
    created_at = 0.0
    
    def __init__(self,id=0,product_id=0,created_at=0.0,price=0.0,price_type_id=0) -> None:
        self.id = id
        self.product_id = product_id
        self.price = price
        self.price_type_id = price_type_id
        self.created_at = created_at

    def toJson(self):
        return {
            product_price_id:self.id,
            product_price_product_id:self.product_id,
            product_price_created_at:self.created_at,
            product_price_price_type_id:self.price_type_id,
            product_price_price:self.price,
        }