



class Colors:

    def __init__(self, color_id: int, color_name: str):
        
        self.id = color_id
        self.color_id = color_id
        self.color_name = color_name

    def __str__(self) -> str:
        return f"{self.id}, {self.color_name}"
    
    # color_id		serial primary key,
	# color_name		varchar(255)