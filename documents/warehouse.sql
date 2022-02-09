DROP DATABASE IF EXISTS warehouse;
CREATE DATABASE IF NOT EXISTS warehouse; 
USE warehouse;

DROP TABLE IF EXISTS Products, Customers, Staffs, Orders;

CREATE TABLE Products (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  `price` FLOAT NOT NULL,
  `amount` INT NOT NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE Customers (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `street` VARCHAR(150) NOT NULL,
  `post_code` INT NOT NULL,
  `age` INT NOT NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `last_name` (`last_name` ASC, `first_name` ASC) INVISIBLE)
ENGINE = InnoDB;

CREATE TABLE Staffs (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `employee_since` DATE NOT NULL,
  `age` INT NOT NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `last_name` (`last_name` ASC, `first_name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE Orders (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `staff_id` INT NOT NULL,
  `count` INT NOT NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `product_tbl_idx` (`product_id` ASC) VISIBLE,
  INDEX `customer_tbl_idx` (`customer_id` ASC) VISIBLE,
  INDEX `staff_tbl_idx` (`staff_id` ASC) VISIBLE,
  CONSTRAINT `product_tbl`
    FOREIGN KEY (`product_id`)
    REFERENCES `warehouse`.`Products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `customer_tbl`
    FOREIGN KEY (`customer_id`)
    REFERENCES `warehouse`.`Customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `staff_tbl`
    FOREIGN KEY (`staff_id`)
    REFERENCES `warehouse`.`Staffs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into Products values (1001,'Såg',129.94,87,'2022-01-10','2022-01-10'),
	(1002,'Hammare',124.80,100,'2022-01-10','2022-01-10'),
    (1003,'Borra',329.95,40,'2022-01-10','2022-01-10'),
    (1004,'Skruva',4.20,1500,'2022-01-10','2022-01-10'),
    (1005,'stift',3.90,3000,'2022-01-10','2022-01-10'),
    (1006,'klämma',322.60,15,'2022-01-10','2022-01-10'),
    (1007,'skruvmejsel',29.40,80,'2022-01-10','2022-01-10'),
    (1008,'skiftnyckel',22.90,95,'2022-01-10','2022-01-10');
    
insert into Customers values 
	(101,'Bezalel','Simmel','Stockholm',12345,45,'2022-01-10','2022-01-10'),
	(102,'Parto','Bamford','Kristianstad',32452,34,'2022-01-10','2022-01-10'),
    (103,'Chirstian','Koblick','Gothenburg',12332,33,'2022-01-10','2022-01-10'),
    (104,'Kyoichi','Maliniak','Malmö',87490,40,'2022-01-10','2022-01-10'),
    (105,'Anneke','Preusig','Stockholm',45637,30,'2022-01-10','2022-01-10'),
	(106,'Tzvetan','Zielinski','Gothenburg',12093,41,'2022-01-10','2022-01-10'),
	(107,'Saniya','Kalloufi','Växjö',76503,38,'2022-01-10','2022-01-10'),
	(108,'Sumant','Peac','Gothenburg',43676,35,'2022-01-10','2022-01-10'),
	(109,'Duangkaew','Piveteau','Stockholm',12121,35,'2022-01-10','2022-01-10'),
	(110,'Mary','Sluis','Malmö',98930,42,'2022-01-10','2022-01-10');
    
insert into Staffs values (1001,'Prasadram','Heyers','2018-03-14',34,'2022-01-10','2022-01-10'),
	(1002,'Yongqiao','Berztiss','2019-07-24',30,'2022-01-10','2022-01-10'),
	(1003,'Elvis','Demeyer','2009-03-15',28,'2022-01-10','2022-01-10'),
	(1004,'Bader','Swan','2016-03-20',35,'2022-01-10','2022-01-10'),
	(1005,'Alain','Chappelet','2020-03-01',34,'2022-01-10','2022-01-10');
    
insert into Orders values 
	(1,1002,103,1002,1,'2022-01-10','2022-01-10'),
	(2,1004,103,1002,10,'2022-01-10','2022-01-10'),
    (3,1004,105,1004,15,'2022-01-10','2022-01-10'),
    (4,1004,107,1005,10,'2022-01-10','2022-01-10'),
    (5,1004,105,1005,15,'2022-01-10','2022-01-10'),
    (6,1004,104,1004,12,'2022-01-10','2022-01-10'),
    (7,1004,101,1002,10,'2022-01-10','2022-01-10'),
    (8,1008,109,1001,2,'2022-01-10','2022-01-10'),
    (9,1003,110,1003,1,'2022-01-10','2022-01-10'),
    (10,1001,106,1001,1,'2022-01-10','2022-01-10'),
    (11,1005,103,1001,3,'2022-01-10','2022-01-10'),
    (12,1007,109,1002,2,'2022-01-10','2022-01-10');