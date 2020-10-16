create view vmovies1970.movies as
	select * from movies where year between 1970 and 1979;
	
create view vmovies1980.movies as
	select * from movies where year between 1980 and 1989;
	
create view vmovies1990.movies as
	select * from movies where year between 1990 and 1999;
	
create view vmovies2000.movies as
	select * from movies where year between 2000 and 2009;

create view vmovies2010.movies as
	select * from movies where year between 2010 and 2019;

create view vmovies2020.movies as
	select * from movies where year between 2020 and 2029;	