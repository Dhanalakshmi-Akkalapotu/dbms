Q1='''SELECT a.id,fname,lname,gender FROM ACTOR  a INNER JOIN 
        cast c ON  a.id=c.pid INNER JOIN Movie ON c.mid=Movie.id
        where name LIKE 'Annie%' GROUP BY a.id;''' 
        
Q2='''SELECT m.id,name,rank,year FROM Movie m INNER JOIN MovieDirector md
        ON m.id=md.mid INNER JOIN Director d ON d.id=md.did
        where year in (1999,1994,2003) and d.fname LIKE 'Biff%'
         and d.lname LIKE 'Malibu%' order by rank desc,year asc;'''     

Q3='''SELECT year,COUNT(id) as no_of_movies FROM Movie group by year
        having AVG(rank) >(SELECT AVG(rank) FROM movie) order by year asc;''' 

Q4='''SELECT id,name,year,rank FROM Movie  where year=2001
        and rank<(SELECT AVG(rank) FROM Movie where year=2001)
        order by rank desc limit 10;'''
        
Q5='''SELECT m.id from movie m                                                                                                                                                                                                                                                                                                                              
       order by m.id asc limit 100;'''
        
Q6='''SELECT DISTINCT pid  from cast INNER JOIN Movie M 
        ON mid =m.id  group by mid,pid 
       having count(DISTINCT role)>1 ORDER BY pid asc LIMIT 100;'''        

Q7='''SELECT fname,count(id) as count from director                                                                                                                                                                                                                                                                                                                                                                                                    
        GROUP BY  fname having count(fname)>1;''' 
        
Q8='''SELECT D.id,fname,lname FROM Director d where exists
        (select * from cast c INNER JOIN MovieDirector
       md on  c.mid=md.mid  where md.did=d.id
       group by c.mid,md.did having count(DISTINCT c.PID)>=100) and not exists 
       (select * from cast c INNER JOIN MovieDirector
       md on  c.mid=md.mid  where md.did=d.id
       group by c.mid,md.did having count(DISTINCT c.PID)<100)
       ;'''
