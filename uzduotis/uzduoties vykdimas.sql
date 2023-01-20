CREATE TABLE customer (
    id integer PRIMARY KEY NOT NULL,
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    email VARCHAR(50)
);


CREATE TABLE status (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(50)
);


CREATE TABLE product (
  id INTEGER PRIMARY KEY NOT NULL,
  name VARCHAR(50),
  price DECIMAL(10,2)
);


CREATE TABLE order_ (
    id integer PRIMARY KEY NOT NULL,
    customer_id INTEGER,
    date_ VARCHAR(50),
    status_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer (id),
    FOREIGN KEY (status_id) REFERENCES status (id)
);


CREATE TABLE product_order (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES order_ (id),
    FOREIGN KEY (product_id) REFERENCES product (id)
);



INSERT INTO customer (id, f_name, l_name, email) VALUES (1, "John", "Doe", "johndoe@example.com");
INSERT INTO customer (id, f_name, l_name, email) VALUES (2, "Jane", "Doe", "janedoe@example.com");
INSERT INTO customer (id, f_name, l_name, email) VALUES (3, "Bob", "Smith", "bobsmith@example.com");


INSERT INTO status (id, name) VALUES (1, "Confirmed");
INSERT INTO status (id, name) VALUES (2, "In Progress");
INSERT INTO status (id, name) VALUES (3, "Completed");
INSERT INTO status (id, name) VALUES (4, "Cancelled");


INSERT INTO product (id, name, price) VALUES (1, "potatoes", 25.99);
INSERT INTO product (id, name, price) VALUES (2, "bananas", 30.99);
INSERT INTO product (id, name, price) VALUES (3, "Oranges", 40.99);
INSERT INTO product (id, name, price) VALUES (4, "Water", 99.99);


INSERT INTO order_ (id, customer_id, date_, status_id) VALUES (1, 1, "2022-01-01", 1);
INSERT INTO order_ (id, customer_id, date_, status_id) VALUES (2, 2, "2022-01-02", 2);
INSERT INTO order_ (id, customer_id, date_, status_id) VALUES (3, 3, "2022-01-03", 3);
INSERT INTO order_ (id, customer_id, date_, status_id) VALUES (4, 1, "2022-01-04", 4);
INSERT INTO order_ (id, customer_id, date_, status_id) VALUES (5, 2, "2022-01-05", 1);


INSERT INTO product_order (order_id, product_id, quantity) VALUES (1, 1, 2);
INSERT INTO product_order (order_id, product_id, quantity) VALUES (1, 2, 1);
INSERT INTO product_order (order_id, product_id, quantity) VALUES (2, 3, 3);
INSERT INTO product_order (order_id, product_id, quantity) VALUES (3, 1, 1);
INSERT INTO product_order (order_id, product_id, quantity) VALUES (4, 2, 2);
INSERT INTO product_order (order_id, product_id, quantity) VALUES (5, 3, 1);









SELECT order_.id as id, customer.l_name as customer, order_.date_ as date,  
SUM(product.price * product_order.quantity) AS total_cost
    FROM order_
    JOIN customer ON order_.customer_id = customer.id
    JOIN product_order ON order_.id = product_order.order_id
    JOIN product ON product_order.product_id = product.id
    GROUP BY order_.id;


SELECT order_.id, product.name, product_order.quantity, product.price, 
(product.price * product_order.quantity) AS total_cost
    FROM order_
    JOIN product_order ON order_.id = product_order.order_id
    JOIN product ON product_order.product_id = product.id;



SELECT order_.id, product.name, 
sum(product_order.quantity) as "Quantity", product.price, 
sum(product_order.quantity) * product.price as "Total"
    FROM order_
    JOIN product_order ON order_.id = product_order.order_id
    JOIN product ON product.id = product_order.product_id
    group by product_order.product_id