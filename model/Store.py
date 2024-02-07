

from . import Addreses

class Store:

    def __init__(self, store_id, store_name, store_addr_id: Addreses):
        self.id = store_id
        self.store_id = store_id
        self.store_name = store_name
        self.store_addr_id = store_addr_id
        
    def __str__(self) -> str:
        return f"{self.store_id} {self.store_name} {self.store_addr_id}"

#   store_id		serial primary key,
# 	store_name		varchar(255),
# 	store_addr_id int,