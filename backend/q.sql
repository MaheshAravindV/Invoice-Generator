customer master:

gstin_no (primary key)
name
address
place_of_supply
state_code
contact_no
contact_email

create table customer_master(
gstin_no char(15) primary key,
name varchar(50) not null,
address varchar(200) not null,
place_of_supply varchar(50) not null,
state_code char(2) not null,
contact_no char(10) not null,
contact_email varchar(50) not null   
);

create table material_master(
hsncode char(15) primary key,
material_detail varchar(50) not null,
uom varchar(10) not null,
rate integer not null,
tax_detail decimal(4,2) not null
);

create table stock_register(
dc_no varchar(20) primary key,
hsncode char(15),
date_of_process date not null,
process char(3) not null,
qty int not null,
foreign key (hsncode) references material_master(hsncode)
);

