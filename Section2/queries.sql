-- Output list of cust and their spending
select c.customerID, c.name as customer_name, SUM(car.price) as total_spending
from transaction t
join customer c on t.customerID = c.customerID
join car on t.car_sn = car.serial_number
group by c.customerID, c.name;

-- Output top 3 car manufactures by sales
select m.name as manufacturer_name, count(t.car_sn) as cars_sold
from transaction t
join car on t.car_sn = car.serial_number
join manufacturer m on car.manufacturer = m.name
group by m.name
order by cars_sold desc
limit 3;