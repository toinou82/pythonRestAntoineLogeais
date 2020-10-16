-- dbmovie (or any other database must be created before)
-- psql -U postgres -d dbmovie -f pg_cine.sql
SET CLIENT_ENCODING = 'UTF-8';

-- cleanup previous data
DROP SCHEMA movie cascade;
-- cleanup user if not used anymore
DROP USER if exists movie;

-- (re) create user
create user movie LOGIN password 'password';

-- create schema with the user name
create schema movie authorization movie;

-- play the following orders as user movie
set role movie;

-- DDL : tables, views
\i pg_cine_ddl.sql;
-- DATA: psql is in no transaction mode by default
\i cine_data_stars.sql;
\i cine_data_movies.sql;
\i cine_data_play.sql;