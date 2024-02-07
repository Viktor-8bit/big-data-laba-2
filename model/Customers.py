
from . import Addreses

class Customers:

    def __init__(self, customer_id: int, last_name: str, first_name: str, middle_name: str, customer_addr_id: Addreses) -> None:
        
        self.id = customer_id
        self.customer_id = customer_id
        
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        
        self.customer_addr_id = customer_addr_id

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.last_name, self.first_name, self.middle_name, self.customer_addr_id)
    # customer_id 	serial primary key,
	
	# last_name		 varchar(255), 		-- имя
	# first_name 		 varchar(255), 		-- фамилия
	# middle_name 	 varchar(255) null, -- отчество
	
	# customer_addr_id int,