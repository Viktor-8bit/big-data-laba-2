


from . import Product
from . import Store

class StoreProduct:
    
    def __init__(self, store_product_id: int, product_id: Product, store_id: Store, product_count: int) -> None:
        self.id = store_product_id
        self.store_product_id = store_product_id
        self.product_id = product_id
        self.store_id = store_id
        self.product_count = product_count

    def __str__(self) -> str:
        return f'{self.store_product_id} {self.product_id} {self.store_id}'


	# store_product_id serial primary key,
	# product_id      int,
	# store_id      	int,
	# product_count   int