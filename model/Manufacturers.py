



class Manufacturers:

    def __init__(self, manufacturer_id: int, manufacturer_name: str):
        
        self.id = manufacturer_id
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name

    def __str__(self) -> str:
        return f"{self.id}, {self.manufacturer_name}, {self.manufacturer_id}"

    # manufacturer_id		serial primary key,
	# manufacturer_name	varchar(255)