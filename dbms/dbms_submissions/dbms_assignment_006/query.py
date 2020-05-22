iBHubs

Home
AssignmentID - DB006
Submission Guidelines
Coding Guidelines
# Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_006. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_006

#Coding Guidelines
Write your queries query.py

Query for each question is to be assigned to a variable in the above python file. Variables for each question are specific individually.

Get fname and lname all the actors casted in movie_id = 12148

Q1="Write your query here"
...

Count the number of movies in which actor “Harrison (I) Ford” acted
first name: “Harrison (I)”
last name: “Ford”
...
Q2="Write your query here"
...


Get all the distinct actors ids who acted in all movie whose title starts with Young Latin Girls.
...
Q3="Write your query here"
...


How many distinct actors have acted in any movie between 1990 and 2000 (both inclusive).
...
Q4="Write your query here"
...





Q1="SELECT fname,lname from actor inner join cast on  id=pid where mid=12148;"

Q2="SELECT COUNT(mid) from actor inner join cast on id=pid where fname='Harrison (I)' and lname='Ford';"

Q3="SELECT DISTINCT pid from cast inner join movie on id=mid where name like 'Young Latin Girls%';"

Q4="SELECT COUNT(DISTINCT pid) from cast inner join movie on id=mid where year between 1990 and 2000;"
