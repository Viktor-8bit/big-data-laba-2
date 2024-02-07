


class Addreses:

    # adress_id, city, street, building_number, apartment_number, entrance_number, additional_info
    def __init__(self, adress_id: int, city: str, street: str,
        building_number: str, apartment_number: str, entrance_number: str, additional_info: str):
        
        self.id = adress_id
        self.adress_id = adress_id
        self.city = city
        self.street = street
        self.building_number = building_number
        self.apartment_number = apartment_number
        self.entrance_number = entrance_number
        self.additional_info = additional_info

    def __str__(self) -> str:
        return "{}, {}, {}, {}, {}, {}, {}".format(self.id, self.city, self.street, self.building_number, self.apartment_number, self.entrance_number, self.additional_info)
# adress_id 			serial primary key,
# city 				varchar(100),		-- город
# street 				varchar(100),	-- улица
# building_number		varchar(10), 	-- номер дома
# apartment_number 	varchar(10), 		-- номер квартиры
# entrance_number  	varchar(10) null, 	-- номер подъезда
# additional_info 	varchar(200) 		-- доп информация