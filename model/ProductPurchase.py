

from . import Product
from . import Purchase

class ProductPurchase:

    def __init__(self, product_purchase_id: int, product_id: Product, purchase_id: Purchase) -> None:
        
        self.id = product_purchase_id
        self.product_purchase_id = product_purchase_id
        self.product_id = product_id
        self.purchase_id = purchase_id

    def __str__(self) -> str:
        return f"{self.product_purchase_id}, {self.product_id}, {self.purchase_id}"
    


    # product_purchase_id serial primary key,
	# product_id 				int,
    # purchase_id 			int,