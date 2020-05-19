Q1='''SELECT p.player_id,m.team_id,p.jersey_no,p.name,p.date_of_birth,p.age
                FROM Player P INNER JOIN MatchCaptain M ON P.Player_id=m.captain
                left JOIN  GoalDetails G ON  M.captain=g.Player_id 
                where  g.goal_id is Null ;'''

Q2='''SELECT t.team_id,count(match_no) as no_of_games from MatchTeamDetails m
        inner join team t on m.team_id=t.team_id group by t.team_id;'''

Q3='''SELECT team_id,(count(goal_id)* 1.0/(SELECT COUNT(Player_id) FROM PLAYER
        group by team_id)) as avg_goal_score from GoalDetails 
      group by team_id ;'''
        
Q4='''SELECT M.captain,count(m.match_no) as no_of_times_captain
        from MatchCaptain  m group by m.captain;'''

Q5='''SELECT count(DISTINCT captain) as no_players from player p INNER JOIN
        Match M ON P.player_id=M.player_of_match INNER JOIN 
        MatchCaptain MC ON  P.player_id=MC.captain 
        and m.match_no=mc.match_no;'''

Q6='''SELECT DISTINCT player_id  FROM player p where exists
        (select * from MatchCaptain mc where p.player_id=mc.captain)
        and not exists(select * from match m where P.player_id=M.player_of_match) ;'''

Q7='''SELECT strftime('%m',play_date) as month, count(match_no)
        as no_of_matches  from match group by month 
        order by no_of_matches desc; '''
                
Q8='''SELECT jersey_no,count(captain) as no_captains from player p
        inner join MatchCaptain mc  on p.player_id=mc.captain group by jersey_no 
        order by no_captains desc,jersey_no desc;'''
        
Q9='''SELECT p.Player_id,AVG(audience) as avg_audience from match m inner join
        player p on p.team_id=mc.team_id  inner join MatchCaptain mc
         on mc.match_no=m.match_no group by p.player_id 
        order by avg_audience desc, p.player_id desc;'''

Q10='''SELECT team_id,AVG(AGE) FROM PLAYER GROUP BY team_id;'''        
                                   
Q11='''SELECT AVG(AGE) as avg_age_of_captains  FROM PLAYER P INNER
        JOIN MatchCaptain M ON M.captain=P.Player_id'''
        
Q12='''SELECT strftime('%m', date_of_birth) as month,COUNT(p.Player_id) AS 
        no_of_players from player p  group by month 
        order by no_of_players desc,month desc;'''

Q13='''SELECT captain,count(m.match_no) as no_of_wins from MatchTeamDetails m
        inner join MatchCaptain mc on m.match_no=mc.match_no
        where win_lose='W' and m.team_id= mc.team_id group by captain order by no_of_wins desc;'''
        