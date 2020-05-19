Q1="SELECT fname,lname from actor inner join cast on  id=pid where mid=12148;"

Q2="SELECT COUNT(mid) from actor inner join cast on id=pid where fname='Harrison (I)' and lname='Ford';"

Q3="SELECT DISTINCT pid from cast inner join movie on id=mid where name like 'Young Latin Girls%';"

Q4="SELECT COUNT(DISTINCT pid) from cast inner join movie on id=mid where year between 1990 and 2000;"
