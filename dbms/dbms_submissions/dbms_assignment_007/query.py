Q1='''SELECT COUNT(id) FROM Movie WHERE year<2000;'''

Q2='''SELECT AVG(rank) FROM Movie where year=1991;'''

Q3='''SELECT MIN(rank) FROM Movie WHERE year=1991 GROUP BY year;'''

Q4='''SELECT fname,lname FROM cast INNER JOIN ACTOR ON id=pid WHERE mid=27;'''

Q5='''SELECT COUNT(mid) FROM Cast INNER JOIN ACTOR ON id=pid WHERE fname='Jon' and lname='Dough';'''

Q6='''SELECT name FROM Movie WHERE name LIKE 'Young Latin Girls%' and (year BETWEEN 2003 AND 2006);'''

Q7='''SELECT Director.fname,Director.lname FROM Director INNER JOIN MovieDirector
        on `Director`.id=`MovieDirector`.did INNER JOIN Movie 
        ON `MovieDirector`.mid=`Movie`.id WHERE Movie.name LIKE 'Star Trek%';'''

Q8='''SELECT name FROM Movie INNER JOIN MovieDirector on `Movie`.id=`MovieDirector`.mid
    INNER JOIN Cast on `Movie`.id =`Cast`.mid 
    INNER JOIN Director on `Director`.id=`MovieDirector`.did
    INNER JOIN Actor on `Actor`.id=`Cast`.pid
    WHERE (`Actor`.fname = 'Jackie (I)' AND `Director`.fname = 'Jackie (I)') AND (`Actor`.lname = 'Chan' AND `Director`.lname = 'Chan') ORDER BY Movie.name ASC;'''

Q9='''SELECT fname, lname 
    FROM Director INNER JOIN MovieDirector ON Director.id=did 
    INNER JOIN Movie ON Movie.id=mid 
    WHERE year = 2001 GROUP BY did Having Count(mid)>=4 ORDER BY fname ASC,lname DESC;'''

Q10='''SELECT gender,COUNT(id) FROM ACTOR  WHERE gender='F' OR gender='M' GROUP BY gender ORDER BY gender ASC;'''


Q11='''SELECT DISTINCT m1.name, m2.name, m1.rank, m1.year FROM Movie m1, Movie m2 
    WHERE (m1.rank == m2.rank AND m1.year == m2.year AND m1.name <> m2.name) ORDER BY m1.name ASC LIMIT 100;'''

Q12='''SELECT fname, year, AVG(rank) 
    FROM Movie INNER JOIN Cast ON `Movie`.id=`Cast`.mid 
    INNER JOIN Actor ON `Actor`.id=`Cast`.pid 
    GROUP BY `Movie`.year, `Actor`.id ORDER BY `Actor`.fname ASC,`Movie`.year DESC LIMIT 100;'''

Q13='''SELECT `Actor`.fname, `DIRECTOR`.fname, AVG(rank)
    FROM Actor INNER JOIN Cast ON `Actor`.id=`Cast`.pid 
    INNER JOIN MovieDirector ON `Cast`.mid=`MovieDirector`.mid
    INNER JOIN Movie ON `MovieDirector`.mid=`Movie`.id
    INNER JOIN Director ON `Director`.id=`MovieDirector`.did
    Group BY `Actor`.id,`Director`.id Having Count(`Cast`.mid)>=5 
    ORDER BY AVG(rank) DESC, `Director`.fname ASC, `Actor`.fname DESC LIMIT 100;'''


'''
Actor (  
	 id integer PRIMARY KEY,
	 fname varchar(250),  
	 lname varchar(250), 
	 gender varchar(10) 
 );

 Movie(  
	 id integer PRIMARY KEY, 
	 name varchar(250), 
	 year integer, 
	 rank integer
 );
	
 Director(  
	 id integer PRIMARY KEY, 
	 fname varchar(250), 
	 lname varchar(250)
 );

Cast(
        pid integer,
        mid integer,
        role varchar(200)
    );

MovieDirector(
        did integer,
        mid integer
    );
'''
