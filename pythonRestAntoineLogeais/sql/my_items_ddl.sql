DROP TABLE if exists items;

create table items (
	id integer auto_increment,
	name varchar(150) not null,
	price decimal(5,2) not null,
	is_offer boolean null,
	constraint pk_items primary key(id)
);