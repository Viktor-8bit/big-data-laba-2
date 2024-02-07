


from . import Purchase


class PurchaseDelivery:

    def __init__(self, purchase_delivery_id: int, delivery_date: str, purchase_id: Purchase):
        
        self.id = purchase_delivery_id
        self.purchase_delivery_id = purchase_delivery_id
        self.delivery_date = delivery_date
        self.purchase_id = purchase_id 

    def __str__(self) -> str:
        return f"{self.purchase_delivery_id}, {self.delivery_date}, {self.purchase_id}"
    


    # purchase_delivery_id	serial primary key,
	# delivery_date       	date,
	# purchase_id         	int,