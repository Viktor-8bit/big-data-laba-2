



-- 1) Выведите самый дорогой и дешевый товар
select * from product 
where (select max(product_price) from product) = product.product_price or 
	  (select min(product_price) from product) = product.product_price;

	 
	 
-- 2) Выведите количество товаров, которое было доставлено с 5 мая 2021 по текущий день.
select count(purchase_id) from purchasedelivery where  purchasedelivery.delivery_date::date >= '2021-05-05'::date
and purchasedelivery.delivery_date::date <= (select CURRENT_DATE)::date;

select * from purchasedelivery order by delivery_date;



/* 3) Выведите производителей, наименования которых начинаются на A, 3ая буква О и
последняя М. */
select * from manufacturers m where m.manufacturer_name like 'A_O%M';



/* 4) Выведите 3ку продуктов с самыми длинными наименованиями, отсортируйте в
алфавитном порядке*/
select p.product_name from 
(select p_max_len.product_name from product p_max_len order by LENGTH(p_max_len.product_name) desc limit 3) 
p order by p.product_name; 



/* 5) Выведите наименования товаров, цена которых изменилась с ноября текущего года. */
select p.product_name  from newprices n 
inner join product p 
on n.product_id = p.product_id
where n.date_price_change >= (SELECT EXTRACT(YEAR FROM CURRENT_DATE)::varchar || '-11-01')::date;  



/* 6) Выведите те категории товаров, которые производит компания Bosh (подзапрос). */
select c.category_name  from category c 
where c.category_id in 
(select p.category_id from product p 
where p.manufacturer_id = (select m.manufacturer_id from manufacturers m where m.manufacturer_name like 'Bosh'));



/* 7) Выведите адреса филиалов компании Samsung (подзапрос) */
select * from addreses a 
where a.adress_id in 
(select s.store_addr_id from store s where s.store_id 
in (select sp.store_id from StoreProduct as sp
where sp.product_id in (select p.product_id from product p 
where p.manufacturer_id = (select m.manufacturer_id  from manufacturers m 
where m.manufacturer_name = 'Samsung')))) group by a.adress_id;




/* 8) Выведите пользователя/лей с самой длинной фамилией. */
select c.first_name, 
	   c.middle_name,
	   c.last_name 
	   from customers c ORDER BY LENGTH(c.last_name) desc LIMIT 1;

	  
	  
/* 9) Выведите самую дорогую и дешевую покупку. */	  
select * from	  
(select
p2.product_name, 
p2.product_size, p2.product_price,
(p2.product_price * (1 - p.discount))::int as "самая дорогая покупка"
from purchase p 
	inner join productpurchase pp on p.purchase_id = pp.purchase_id 
	inner join product p2 on p2.product_id = pp.product_id
	order by (p2.product_price * (1 - p.discount))::int desc limit 1) as one,
(select
p2.product_name, 
p2.product_size, p2.product_price,
(p2.product_price * (1 - p.discount))::int as "самая дешевая покупка"
from purchase p 
	inner join productpurchase pp on p.purchase_id = pp.purchase_id 
	inner join product p2 on p2.product_id = pp.product_id
	order by (p2.product_price * (1 - p.discount))::int asc limit 1) as two;


/* 10) Выведите количество покупателей с одинаковым именем.*/ 
select count(c.customer_id)  from customers c 
		where (select count(c2.customer_id) e from customers c2 where c.first_name = c2.first_name) > 1;

	
	
/* 11) Выведите товары и в каком количестве их доставляли, отсортируйте товары в обратном
алфавитному порядку.*/ 
select (select Count(pd.purchase_delivery_id) as "количество доставок" from purchase p2 
		inner join purchasedelivery pd on p2.purchase_id = pd.purchase_id
		inner join productpurchase pp on pp.purchase_id = p2.purchase_id
		inner join product p3 on pp.product_id = p3.product_id
		where p3.product_id = p.product_id), * from product p order by p.product_name desc;

	
	
/* 12) Выведите покупателей, которые купили более 10 товаров с марта текущего года.*/ 
select c.customer_id, c.last_name, c.first_name, c.middle_name  from customers c inner join purchase p 
on p.customer_id = c.customer_id
where (select count(p2.purchase_id) from purchase p2 
where p2.customer_id = c.customer_id 
and p2.purchase_date >= (SELECT EXTRACT(YEAR FROM CURRENT_DATE)::varchar || '-03-01')::date) >= 10
group by c.customer_id;



/* 13) Выведите категории товаров, которые не производит компания Samsung.*/ 
select c.category_id, c.category_name  from category c 
where c.category_id not in 
(select p.category_id from product p 
where p.manufacturer_id = (select m.manufacturer_id from manufacturers m where m.manufacturer_name like 'Samsung'));




/* 14) Выведите наименование товара и его производителя, доставка которого осуществилась с
филиала «Мира 25» с июня 2021 года по август 2021 года.*/ 
select p.product_name, 
	(select m.manufacturer_name from manufacturers as m where manufacturer_id = p.manufacturer_id)	
	from product p 
	inner join productpurchase as pp on pp.product_id = p.product_id
	where (select (select a.street || a.building_number from addreses a where s.store_addr_id = a.adress_id) 
			from store as s inner join purchase p2 on p2.store_id = s.store_id
			where p2.purchase_id = pp.purchase_id) = 'Мира25'
		and (select count(*) from purchasedelivery as pd
			 where  pd.purchase_id = pp.purchase_id 
			 and extract(year from pd.delivery_date) = 2021
			 and extract(month from pd.delivery_date) = 8) >= 1
		and (select count(*) from purchase as p2
			 where  p2.purchase_id = pp.purchase_id 
			 and extract(year from p2.purchase_date) = 2021
			 and extract(month from p2.purchase_date) = 6) >= 1		 
			 
			 
select delivery_date, purchase_id from purchasedelivery where purchase_id = 46
select (select count(*)  from PurchaseDelivery pd where pd.purchase_id = p.purchase_id ), p.purchase_id from purchase p 




/* 15) Посчитать суммарные продажи по каждому товару (стоимость * количество), вывести 
    наименование товара и итоговую сумму. */ 
select 
	p.product_name, 
	sum( 
		 (select count(*) from productpurchase p3 where p3.product_id = pp.product_id)
		 * p.product_price 
		 * (1 - p2.discount)
		)
from productpurchase pp 
	right join product p on pp.product_id  = p.product_id 
	inner join purchase p2 on p2.purchase_id = pp.purchase_id
	group by p.product_name, pp.product_id; 



/* 16) Выведите производителя и количество проданных товаров данного производителя. */ 
select m.manufacturer_name,
	count(p.product_id)
	from manufacturers m 
	left join product p on p.manufacturer_id = m.manufacturer_id
 	left join productpurchase p2 on p.product_id = p2.product_id
	group by m.manufacturer_name;



/* 17) Выведите суммарное количество товаров, проданных с каждого филиала. */ 
select 
	s.store_name,
	(select 
		a.city || ' ' || 
		a.street || ' ' || 
		a.building_number || ' ' || 
		a.apartment_number || ' ' || 
		a.entrance_number || ' ' || 
		a.additional_info
		from addreses a 
		where a.adress_id = s.store_addr_id
	) as адресс,
	count(p.purchase_id)
	from store s 
	left join purchase p on p.store_id = s.store_id
	group by s.store_name,
	(select 
		a.city || ' ' || 
		a.street || ' ' || 
		a.building_number || ' ' || 
		a.apartment_number || ' ' || 
		a.entrance_number || ' ' || 
		a.additional_info
		from addreses a 
		where a.adress_id = s.store_addr_id
	);


















	  