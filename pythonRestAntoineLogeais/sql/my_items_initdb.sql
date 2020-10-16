-- connect with user root on none (database) 
-- mysql -u root (xampp)
-- sudo mysql -u root (linux without password)
-- mysql -u root -p (linux with password)

-- create database
create database magasin CHARACTER SET utf8;

-- create user with all privileges on previous database
create user mag@localhost identified by 'password';
grant all privileges on magasin.* to 'mag'@'localhost';
flush privileges;

-- connect to magasin database 
use magasin;
