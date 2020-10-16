-- MySQL/MariaDB admin tips

-- NB: if dbname is ommited, connection on None database
-- * connection without password (use sudo on linux)
-- mysql -u username [-h hostname -P port]
-- mysql -u username [-h hostname -P port] dbname
-- * connection with password
-- mysql -u username [-h hostname -P port] -p
-- mysql -u username  [-h hostname -p port] dbname
-- mysql -u username [-h hostname -p port] dbname < my_script.sql

-- commands inside a mysql client

-- play a SQL script
source myscript.sql
-- connect to database
use dbmovie;
-- list databases
show databases;
-- list tables
show tables;
-- list users
select host, user, password from mysql.user;