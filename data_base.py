import random
import psycopg2
from datetime import datetime, timedelta

from model.Manufacturers import Manufacturers
from model.Addreses import Addreses
from model.Colors import Colors
from model.Customers import Customers
from model.Category import Category
from model.Store import Store
from model.Product import Product
from model.NewPrices import NewPrices
from model.StoreProduct import StoreProduct
from model.Purchase import Purchase
from model.PurchaseDelivery import PurchaseDelivery
from model.ProductPurchase import ProductPurchase

# Адреса id [0 - 15]
addresses = [
    Addreses(1, "Saint Petersburg", "Nevsky", "25", "3", "10", "Entrance on the right"),
    Addreses(2, "Moscow", "Kirova", "12", "1", "2", "Entrance on the left"),
    Addreses(3, "New York", "Broadway", "45", "5", "A", "Main entrance"),
    Addreses(4, "Tokyo", "Shibuya", "8", "B", "1", "Side entrance"),
    Addreses(5, "Paris", "Champs-Elysees", "30", "2", "C", "Back entrance"),
    Addreses(6, "London", "Baker Street", "221B", "Ground", "1", "Front entrance"),
    Addreses(7, "Berlin", "Alexanderplatz", "1", "-", "3", "Service entrance"),
    Addreses(8, "Sydney", "George Street", "100", "Level 1", "Suite 5", "Employee entrance"),
    Addreses(9, "Rome", "Via Condotti", "10", "A", "6", "Delivery entrance"),
    Addreses(10, "Dubai", "Sheikh Zayed Road", "123", "Tower A", "Floor 15", "Guest entrance"),
    Addreses(11, "Los Angeles", "Hollywood Boulevard", "555", "Penthouse", "Top Floor", "VIP entrance"),
    Addreses(12, "Singapore", "Orchard Road", "40", "Lobby", "Level 3", "Exclusive entrance"),
    Addreses(13, "Toronto", "Yonge Street", "80", "Unit 200", "Suite 2", "Private entrance"),
    Addreses(14, "Berlin", "Potsdamer Platz", "1", "-", "15", "Restricted entrance"),
    Addreses(15, "Barcelona", "Paseo de Gracia", "75", "Floor 2", "Door 7", "Secret entrance")
]

# Производители id [0 - 15]
manufacturers = [ 
    Manufacturers(0, "PepsiCo 🥤"),
    Manufacturers(1, "Samsung 📱"), 
    Manufacturers(2, "Toyota 🚗"), 
    Manufacturers(3, "Nike 👟"), 
    Manufacturers(4, "Coca-Cola 🥤"), 
    Manufacturers(5, "Microsoft 💻"), 
    Manufacturers(6, "Adidas 👟"), 
    Manufacturers(7, "Ford 🚗"), 
    Manufacturers(8, "Google  🌐"),
    Manufacturers(9, "Amazon 📦"), 
    Manufacturers(10, "BMW 🚗"), 
    Manufacturers(11, "Intel 💻"), 
    Manufacturers(12, "McDonald's 🍔"),
    Manufacturers(13, "Honda 🚗"), 
    Manufacturers(14, "Sony 📺"), 
]

# Цвета id [0 - 15]
colors = [
    Colors(1, "red"),
    Colors(2, "blue"),
    Colors(3, "green"),
    Colors(4, "yellow"),
    Colors(5, "purple"),
    Colors(6, "orange"),
    Colors(7, "pink"),
    Colors(8, "brown"),
    Colors(9, "gray"),
    Colors(10, "white"),
    Colors(11, "cyan"),
    Colors(12, "magenta"),
    Colors(13, "teal"),
    Colors(14, "lime"),
    Colors(15, "indigo")
]

# Покупатели id [0 - 15]
customers = [
    Customers(0, "Генадий", "Ганадиев", "Генадиевич", addresses[0]),
    Customers(1, "Иван", "Иванов", "Иванович", addresses[0]),
    Customers(2, "Петр", "Петров", "Петрович", addresses[1]),
    Customers(3, "Мария", "Сидорова", "Ивановна", addresses[2]),
    Customers(4, "Алексей", "Смирнов", "Петрович", addresses[3]),
    Customers(5, "Елена", "Козлова", "Алексеевна", addresses[4]),
    Customers(6, "Андрей", "Николаев", "Сергеевич", addresses[5]),
    Customers(7, "Юлия", "Павлова", "Дмитриевна", addresses[6]),
    Customers(8, "Дмитрий", "Васильев", "Андреевич", addresses[7]),
    Customers(9, "Ольга", "Александрова", "Петровна", addresses[8]),
    Customers(10, "Сергей", "Михайлов", "Александрович", addresses[9]),
    Customers(11, "Наталья", "Егорова", "Владимировна", addresses[10]),
    Customers(12, "Александра", "Никитина", "Алексеевна", addresses[11]),
    Customers(13, "Владимир", "Андреев", "Владимирович", addresses[12]),
    Customers(14, "Татьяна", "Степанова", "Владимировна", addresses[13]),
    Customers(15, "Игорь", "Николаев", "Игоревич", addresses[14])
]

# Категории id [0 - 15]
categories = [
    Category(1, "Smartphone"),
    Category(2, "Tablet"),
    Category(3, "Headphones"),
    Category(4, "Smartwatch"),
    Category(5, "Camera"),
    Category(6, "TV"),
    Category(7, "Gaming Console"),
    Category(8, "Printer"),
    Category(9, "Monitor"),
    Category(10, "Router"),
    Category(11, "Keyboard"),
    Category(12, "Mouse"),
    Category(13, "Smart Home Device"),
    Category(14, "Fitness Tracker"),
    Category(15, "External Hard Drive"),
    Category(16, "Software")
]

# Магазины id [0 - 15]
stores = []
for i in range(15):
    store = Store(i, "Store", addresses[i])
    stores.append(store)

# Продукты id [0 - 15]
products = [
    Product(0, random.randint(1, 2700), random.randint(1, 27000000), "iPhone 11", categories[0], colors[0], manufacturers[0]),
    Product(1, random.randint(1, 27000000), random.randint(1, 27000000), "Samsung Galaxy S21", categories[1], colors[1], manufacturers[1]),
    Product(2, random.randint(1, 27000000), random.randint(1, 27000000), "Google Pixel 6", categories[2], colors[2], manufacturers[2]),
    Product(3, random.randint(1, 27000000), random.randint(1, 27000000), "OnePlus 9 Pro", categories[3], colors[3], manufacturers[3]),
    Product(4, random.randint(1, 27000000), random.randint(1, 27000000), "Xiaomi Mi 11", categories[4], colors[4], manufacturers[4]),
    Product(5, random.randint(1, 27000000), random.randint(1, 27000000), "Huawei P40 Pro", categories[5], colors[5], manufacturers[5]),
    Product(6, random.randint(1, 27000000), random.randint(1, 27000000), "Sony Xperia 1 III", categories[6], colors[6], manufacturers[6]),
    Product(7, random.randint(1, 27000000), random.randint(1, 27000000), "LG Velvet 5G", categories[7], colors[7], manufacturers[7]),
    Product(8, random.randint(1, 27000000), random.randint(1, 27000000), "Oppo Find X3 Pro", categories[8], colors[8], manufacturers[8]),
    Product(9, random.randint(1, 27000000), random.randint(1, 27000000), "Motorola Edge Plus", categories[9], colors[9], manufacturers[9]),
    Product(10, random.randint(1, 27000000), random.randint(1, 27000000), "BlackBerry Key2", categories[10], colors[10], manufacturers[10]),
    Product(11, random.randint(1, 27000000), random.randint(1, 27000000), "Nokia 8.3 5G", categories[11], colors[11], manufacturers[11]),
    Product(12, random.randint(1, 27000000), random.randint(1, 27000000), "ASUS ROG Phone 5", categories[12], colors[12], manufacturers[12]),
    Product(13, random.randint(1, 27000000), random.randint(1, 27000000), "HTC U20 5G", categories[13], colors[13], manufacturers[13]),
    Product(14, random.randint(1, 27000000), random.randint(1, 27000000), "Lenovo Legion Phone Duel 2", categories[14], colors[14], manufacturers[14])
]

# Новые цены id [0 - 15]
start_date = datetime(1900, 1, 1)
end_date = datetime(2023, 12, 31)
newprices = []
id = 0
for p in products:
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    newprices.append(NewPrices(id, f"{random_date.year}-{random_date.month}-{random_date.day}", random.randint(1, 27000000), products[id]))
    id += 1

# Склады id [0 - 15]
id = 0
productstories = []
for s in stores:
    for p in products:
        productstories.append(StoreProduct(id, p, s, random.randint(0, 5)))
        id += 1

# Чеки id [0 - 15]
id = 0
start_date = datetime(1900, 1, 1)
end_date = datetime(2011, 12, 31)
purchases = []
for c in customers:
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    purchases.append(Purchase(id, random.randint(10, 100) / 100, f"{random_date.year}-{random_date.month}-{random_date.day}", c, random.choice(stores))) 
    id += 1

# Доставка id [0 - 15]
id = 0
start_date = datetime(2011, 12, 31)
end_date = datetime(2025, 12, 31)
purchasedelivery = []
for p in purchases:
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    purchasedelivery.append(PurchaseDelivery(id, f"{random_date.year}-{random_date.month}-{random_date.day}", p))
    id += 1

# Покупки
id = 0
productpurchase = []
for p in purchases:
    productpurchase.append(ProductPurchase(id, random.choice(products), p))
    id += 1

# Connect to an existing database
conn = psycopg2.connect("dbname=postgres user=postgres password=rDx-Ckr-PjM-373 host=localhost port=5432")

# Open a cursor to perform database operations
cur = conn.cursor()

# Category
for c in categories:
    cur.execute("INSERT INTO Category (category_id, category_name) VALUES (%s, %s)", (c.category_id, c.category_name))

# Manufacturers
for m in manufacturers:
    cur.execute("INSERT INTO Manufacturers (manufacturer_id, manufacturer_name) VALUES (%s, %s)", (m.manufacturer_id, m.manufacturer_name))

# Addreses
for a in addresses:
    cur.execute("""INSERT INTO Addreses (adress_id, city, street, building_number, apartment_number, entrance_number, additional_info) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)""", (a.adress_id, a.city,  a.street, a.building_number, a.apartment_number, a.entrance_number, a.additional_info))

# Customers
for c in customers:
    cur.execute("""INSERT INTO Customers (customer_id, last_name, first_name, middle_name, customer_addr_id) 
                VALUES (%s, %s, %s, %s, %s)""", (c.customer_id, c.last_name, c.first_name, c.middle_name, c.customer_addr_id.adress_id))

# Store
for s in stores:
    cur.execute("INSERT INTO Store (store_id, store_name, store_addr_id) VALUES (%s, %s, %s)", (s.store_id, s.store_name, s.store_addr_id.adress_id))

# Colors
for c in colors:
    cur.execute("INSERT INTO Colors (color_id, color_name) VALUES (%s, %s)", (c.color_id, c.color_name))

# Product
for p in products:
    cur.execute("""INSERT INTO Product (product_id, product_size, product_price, product_name, category_id, product_color_id, manufacturer_id)
                VALUES(%s, %s, %s, %s, %s, %s, %s)""", (p.product_id, p.product_size, p.product_price, p.product_name, p.category_id.category_id, p.product_color_id.color_id, p.manufacturer_id.manufacturer_id))

# NewPrices
for np in newprices:
    cur.execute("INSERT INTO NewPrices (new_prices_id, date_price_change, new_price, product_id) VALUES (%s, %s, %s, %s)", (np.new_prices_id, np.date_price_change, np.new_price, np.product_id.product_id))

# StoreProduct
for st in productstories:
    cur.execute("""INSERT INTO StoreProduct (store_product_id, product_id, store_id, product_count) 
                VALUES (%s, %s, %s, %s) """, (st.store_product_id, st.product_id.product_id, st.store_id.store_id, st.product_count))

# Purchase
for p in purchases:
    cur.execute(""" INSERT INTO Purchase (purchase_id, discount, purchase_date, store_id, customer_id)
                VALUES (%s, %s, %s, %s, %s)""", (p.purchase_id, p.discount, p.purchase_date, p.store_id.store_id, p.customer_id.customer_id))

# PurchaseDelivery
for pd in purchasedelivery:
    cur.execute(""" INSERT INTO PurchaseDelivery (purchase_delivery_id, delivery_date, purchase_id)
                VALUES (%s, %s, %s)""", (pd.purchase_delivery_id, pd.delivery_date, pd.purchase_id.purchase_id))

# ProductPurchase
for pp in productpurchase:
    cur.execute(""" INSERT INTO ProductPurchase (product_purchase_id, product_id, purchase_id)
                VALUES (%s, %s, %s)""", (pp.product_purchase_id, pp.product_id.product_id, pp.purchase_id.purchase_id) )


conn.commit()
cur.close()
conn.close()


# print("")
# print("=== Manufacturers ===")
# [print(m) for m in manufacturers]

# print("")
# print("=== Addreses ===")
# [print(a) for a in addresses]

# print("")
# print("=== Colors ===")
# [print(c) for c in colors]

# print("")
# print("=== Categories ===")
# [print(c) for c in categories]

# print("")
# print("=== Customers ===")
# [print(c) for c in customers]

# print("")
# print("=== Stores ===")
# [print(s) for s in stores]

# print("")
# print("=== Products ===")
# [print(p) for p in products]

# print("")
# print("=== NewPrices ===")
# [print(np) for np in newprices]

# print("=== StoreProduct ===")
# [print(sp) for sp in productstories]

# print("")
# print("=== Purchases ===")
# [print(p) for p in purchases]

# print("")
# print("=== PurchaseDelivery ===")
# [print(pd) for pd in purchasedelivery]

# print("")
# print("=== ProductPurchase ===")
# [print(pp) for pp in productpurchase]
