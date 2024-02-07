drop table if exists  PurchaseDelivery;
drop table if exists  ProductPurchase;
drop table if exists  Purchase;
drop table if exists  StoreProduct;
drop table if exists  NewPrices;
drop table if exists  Product;
drop table if exists  Colors;
drop table if exists  Store;
drop table if exists  Customers;
drop table if exists  Addreses;
drop table if exists  Manufacturers;
drop table if exists  Category;

-- ===== Ктегории | Category =====
create table if not exists Category (
	category_id		serial primary key,
	category_name	varchar(255)
);


-- ===== Производители | Manufacturer =====
create table if not exists Manufacturers (
	manufacturer_id		serial primary key,
	manufacturer_name	varchar(255)
);


-- ===== Адреса | Addreses =====
create table if not exists Addreses (
    adress_id 			serial primary key,
    city 				varchar(100),		-- город
    street 				varchar(100),		-- улица
    building_number		varchar(10), 		-- номер дома
    apartment_number 	varchar(10), 		-- номер квартиры
    entrance_number  	varchar(10) null, 	-- номер подъезда
    additional_info 	varchar(200) 		-- доп информация
);


-- ===== Покупатели | Customer =====
create table if not exists Customers (
	customer_id 	serial primary key,
	
	last_name		 varchar(255), 		-- имя
	first_name 		 varchar(255), 		-- фамилия
	middle_name 	 varchar(255) null, -- отчество
	
	customer_addr_id int,
	CONSTRAINT fk_customer_addr_id FOREIGN KEY (customer_addr_id) REFERENCES Addreses(adress_id)
);


-- ===== Магазины | Store =====
create table if not exists Store (
	store_id		serial primary key,
	store_name		varchar(255),
	
	store_addr_id int,
	CONSTRAINT fk_store_addr_id FOREIGN KEY (store_addr_id) REFERENCES Addreses(adress_id)
);


-- ===== Цвета | Colors =====
create table if not exists Colors (
	color_id		serial primary key,
	color_name		varchar(255)
);


-- ===== Продукты | Product =====
create table if not exists Product (
	product_id		serial primary key,
	
	product_size		int,
--	product_count		int,
	product_price		numeric(15, 2),
	product_name		varchar(255),	

	-- store_id 			int,
	-- CONSTRAINT fk_store_id FOREIGN KEY (store_id) REFERENCES Store(store_id),
	
	product_color_id	int,
	CONSTRAINT fk_product_color_id FOREIGN KEY (product_color_id) REFERENCES Colors(color_id),
	
	category_id 		int,
	CONSTRAINT fk_category_id  FOREIGN KEY (category_id) REFERENCES Category(category_id),
	
	manufacturer_id		int,
	CONSTRAINT fk_manufacturer_id  FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id)
);


-- ===== Новая цена | NewPrices =====
create table if not exists NewPrices (
	new_prices_id		serial primary key,
	date_price_change	date,
	new_price			numeric(15, 2),

	product_id			int,
	CONSTRAINT fk_product_id  FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- ===== Магазины-Продукты | StoreProduct =====
create table if not exists StoreProduct (
	
	store_product_id serial primary key,
	
	product_id      int,
	CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES Product(product_id),
	
	store_id      	int,
    CONSTRAINT fk_store_id FOREIGN KEY (store_id) REFERENCES Store(store_id),

	product_count   int

);


-- ===== Покупки | Purchase =====
create table if not exists Purchase (
	purchase_id			serial primary key,
	
	discount			numeric(5, 2),
	
	purchase_date		date,
	
	store_id			int,
	CONSTRAINT fk_store_id  FOREIGN KEY (store_id) REFERENCES Store(store_id),

	customer_id			int,
	CONSTRAINT fk_customer_id  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- ===== Доставки покупок | PurchaseDelivery ===== 
create table if not exists PurchaseDelivery (
	purchase_delivery_id	serial primary key,
	
	delivery_date       	date,
	
	purchase_id         	int,
	CONSTRAINT fk_purchase_id   FOREIGN KEY (purchase_id ) REFERENCES Purchase(purchase_id)
);

-- ===== Продукты-Покупки | ProductPurchase =====
create table if not exists ProductPurchase (
    
	product_purchase_id serial primary key,

	product_id 				int,
    purchase_id 			int,
    
    CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES Product(product_id),
    CONSTRAINT fk_purchase_id FOREIGN KEY (purchase_id) REFERENCES Purchase(purchase_id)
);










