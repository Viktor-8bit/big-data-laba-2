




class Category:

    def __init__(self, category_id: int, category_name: str):
        
        self.id = category_id
        self.category_id = category_id
        self.category_name = category_name
        
    def __str__(self) -> str:
        return f"{self.id}, {self.category_name}"
    
	
    # category_id		serial primary key,
	# category_name	varchar(255)