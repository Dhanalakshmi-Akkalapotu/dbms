iBHubs

Home
AssignmentID - DB008
Submission Guidelines
Coding Guidelines
Questions
Note: You can make use of imdb.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_008. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_008/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specified individually.
#Questions
Get all Budding directors - Find all directors who didn’t direct any film before 2000 and have directed at least one film after 2000. Your query should result in id and fname of the director in ascending order of id.

Sample Output Format:

1 Director1
2 Director2

Query Submission Format:

Q1="Write your query here"


Find the best ranked movie for each director. Incase of more than one movie select the first one when sorted in ascending order of movie name.
Your query should return fname and name of the movie. Your query should return only 100 entries

Sample Output Format:

Director1 Movie1
Director2 Movie2

Query Submission Format:

Q2="Write your query here"

List 100 actors who didn't act in any movie between 1990 and 2000. Your query should return only 100 unique actors when sorted by id in descending order.

Q3="Write your query here"    



Q1='''select d.id,d.fname from director d  where exists( select d.id from moviedirector m inner join movie on m.mid=movie.id  where m.did=d.id and movie.year>2000) and 
        not exists(select d.id from moviedirector m inner join movie on m.mid=movie.id  where m.did=d.id and movie.year<2000) order by d.id asc;'''


Q2='''select fname,(select name from movie inner join moviedirector m on  movie.id=m.mid  where m.did=d.id  order by movie.rank desc limit 1) 
        from director as d  limit 100;'''
        
Q3='''select * from actor where not exists(select `cast`.pid  from cast inner join movie  on `cast`.mid=`movie`.id where `cast`.pid=`actor`.id and `movie`.year between 1990 and 2000) order by `actor`.id desc limit 100;'''      
        
