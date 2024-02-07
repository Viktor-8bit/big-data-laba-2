

from . import Customers
from . import Store

class Purchase:

    def __init__(self, purchase_id: int, discount: float, purchase_date: str, customer_id: Customers, store_id: Store) -> None:
        self.id = purchase_id
        self.purchase_id = purchase_id
        self.discount = discount
        self.purchase_date = purchase_date
        self.customer_id = customer_id
        self.store_id = store_id

    def __str__(self) -> str:
        return f"{self.purchase_id}, {self.discount}, {self.purchase_date}, {self.customer_id}, {self.store_id}"
    
    # purchase_id			serial primary key,
	# discount			numeric(5, 2),
	# purchase_date		date,
	# customer_id			int,
    # store_id			int,