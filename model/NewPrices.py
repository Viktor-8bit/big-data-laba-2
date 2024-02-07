

from . import Product

class NewPrices:

    def __init__(self, new_prices_id: int, date_price_change: str, new_price: float, product_id: Product) -> None:
        
        self.new_prices_id = new_prices_id
        self.date_price_change = date_price_change
        self.new_price = new_price
        self.product_id = product_id

    def __str__(self) -> str:
        return f"{self.new_prices_id}, {self.date_price_change}, {self.new_price}, {self.product_id}"
    

    # new_prices_id		serial primary key,
	# date_price_change	date,
	# new_price			numeric(15, 2),
	# product_id			int,