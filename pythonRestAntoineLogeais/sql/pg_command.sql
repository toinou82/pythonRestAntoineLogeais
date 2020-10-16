-- PostgreSQL admin tips

-- connection
-- psql -U username -d dbname  [-h hostname -p port]
-- psql -U username -d dbname  [-h hostname -p port] -f my_script.sql

-- commands inside a psql client
-- play a sql script
\i myscript.sql
-- list databases
\l
-- list tables
\dt
-- list users
select rolname from pg_roles where rolcanlogin;