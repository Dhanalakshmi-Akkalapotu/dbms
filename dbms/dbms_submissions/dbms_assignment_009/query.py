Q1='''SELECT AVG(age) FROM player;'''

Q2='''SELECT match_no,play_date from match
        where audience>50000 order by match_no asc;'''

Q3='''SELECT team_id,count(match_no) AS det 
        from MatchTeamDetails where win_lose='W' 
        group by team_id order by det DESC,team_id ASC;'''

Q4='''SELECT match_no,play_date FROM Match 
        WHERE stop1_sec>(select AVG(stop1_sec) 
        from match) order by match_no DESC;'''

Q5='''SELECT m.match_no,t.name,p.name from MatchCaptain m 
        inner join team t on m.team_id=t.team_id inner join 
        player p on m.captain=p.player_id  order by match_no ASC,t. name ASC;  '''

Q6='''SELECT m.match_no,p.name,p.jersey_no from player p
    inner join  match m on m.player_of_match=p.player_id
    order by match_no ASC;'''
        
Q7='''SELECT name,(select AVG(age) from player p
        where team.team_id=p.team_id) as avg_age from team  
        where avg_age>26 order by name ASC;'''      
    
Q8='''SELECT p.name,p.jersey_no,p.age,count(goal_id) 
      from player p inner join GoalDetails g on p.player_id=g.player_id  
      where p.age<=27 group by p.player_id 
      having count(goal_id)>=1  order by count(goal_id) DESC, p.name ASC;'''

Q9='''SELECT team_id,count(goal_id)*100.0/ 
      (select count(goal_id) from GoalDetails)from GoalDetails 
      group by team_id having count(goal_id)>=1;'''

Q10='''SELECT AVG(TOTAL_GOALS) 
        FROM(SELECT COUNT(goal_id) as TOTAL_GOALS
        FROM GoalDetails  g group by g.team_id);'''

Q11='''SELECT player_id,name,date_of_birth  from player p 
        where not exists(select * from GoalDetails g 
       where g.player_id=p.player_id) order by p.player_id ASC;'''
       
Q12='''SELECT t.name,m.match_no,m.audience,
            audience - (select avg(audience)  
            from (MatchCaptain mc inner join 
            match m on mc.match_no=m.match_no and mc.team_id=t.team_id))
        from team t inner join  MatchCaptain mc on mc.team_id=t.team_id 
        inner join match m on mc.match_no=m.match_no
        order by m.match_no ASC;'''

