import product as productModule
import pricetype as pricetypeModule
import repository

# table name in db
table_name = "product_price"

# table columns
product_price_id = "id"
product_price_product_id = "product_id"
product_price_price = "price"
product_price_created_at = "created_at"
product_price_price_type_id = "price_type_id"

required_fields_to_create = [product_price_product_id,product_price_price_type_id,product_price_price]

def query_product_price_pricetype(id):
    return f"SELECT * FROM {table_name} WHERE {product_price_price_type_id}={id}"
def query_product_price_product(id):
    return f"SELECT * FROM {table_name} WHERE {product_price_product_id}={id}"
def query_product_price_list(limit,page):
    return f"SELECT * FROM {table_name} ORDER BY {product_price_id} LIMIT {(page-1)*limit},{limit}"
def query_product_price_insert(productprice_object):
    return f"INSERT INTO {table_name} ({product_price_product_id},{product_price_price_type_id},{product_price_price},{product_price_price}) VALUES ({productprice_object.product['id']},{productprice_object.price_type['id']},{productprice_object.price},{productprice_object.created_at})"

class ProductPrice:

    id = 0
    product = None
    price = 0.0
    price_type = None
    created_at = 0.0
    
    def __init__(self,id=0,product_id=0,created_at=0.0,price=0.0,price_type_id=0) -> None:
        self.id = id
        if product_id != 0:
            product = repository.get_product_by_id(product_id,False)
            self.product = product
        else:
            self.product = None
        if price_type_id != 0:
            price_type = repository.get_pricetype_by_id(price_type_id,False)
            self.price_type = price_type
        else:
            self.price_type = None
        self.created_at = created_at
        self.price = price

    def toJson(self):
        return {
            product_price_id:self.id,
            productModule.table_name:self.product,
            product_price_created_at:self.created_at,
            pricetypeModule.table_name:self.price_type,
            product_price_price:self.price,
        }