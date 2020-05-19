Q1='''select d.id,d.fname from director d  where exists( select d.id from moviedirector m inner join movie on m.mid=movie.id  where m.did=d.id and movie.year>2000) and 
        not exists(select d.id from moviedirector m inner join movie on m.mid=movie.id  where m.did=d.id and movie.year<2000) order by d.id asc;'''


Q2='''select fname,(select name from movie inner join moviedirector m on  movie.id=m.mid  where m.did=d.id  order by movie.rank desc limit 1) 
        from director as d  limit 100;'''
        
Q3='''select * from actor where not exists(select `cast`.pid  from cast inner join movie  on `cast`.mid=`movie`.id where `cast`.pid=`actor`.id and `movie`.year between 1990 and 2000) order by `actor`.id desc limit 100;'''      
        