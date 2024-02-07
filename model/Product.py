

from . import Colors
from . import Manufacturers
from . import Category

class Product:

    def __init__(self, product_id: int, product_size: int, product_price: float,  
                 product_name: str, category_id: Category, product_color_id: Colors, manufacturer_id: Manufacturers) -> None:
        
        self.id = product_id
        self.product_id = product_id

        self.product_size = product_size
        self.product_price = product_price
        self.product_name = product_name

        self.category_id = category_id
        self.product_color_id = product_color_id
        self.manufacturer_id = manufacturer_id

    def __str__(self) -> str:
        return f"""{self.id}, {self.product_name}, {self.product_price}, {self.product_size}, {self.product_color_id}, {self.category_id}, {self.manufacturer_id}"""
    

    # product_id		serial primary key,
	
	# product_size		int,
	# product_price		numeric(15, 2),
	# product_name		varchar(255),		
	# product_color_id	int,	
	# category_id 		int,
	# manufacturer_id	int,
	