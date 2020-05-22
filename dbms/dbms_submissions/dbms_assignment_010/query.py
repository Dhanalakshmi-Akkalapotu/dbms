iBHubs

Home
AssignmentID - DB019
Submission Guidelines
Know your data
Query Submission Guideline
Questions
Task 1
Task 2
Task 3
Task 4
Task 5
Task 6
Task 7
Task 8
Task 9
Task 10
Task 11
Task 12
Task 13
Note: You can make use of soccer.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/database_submissions/dbms_assignment_010. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/database_submissions/dbms_assignment_010/

# Know your data


Tables:

Team
Match
Player
MatchTeamDetails:
MatchCaptain
GoalDetails
Coding Guidelines:

Write your queries in query.py
Query for each question is to be assigned to a variable in the above metioned python file.
# Query Submission Guideline
Assign your query string to a variable with name have the following format

Q{question Number}="Write your query here"

Below are variable names for question 1 and 2 queries

Q1="Write your query here"
Q2="Write your query here"

#Questions
# Task 1
Find all the players in the database who acted as captain for at-least one match and didn't make at least one goal.

# Sample Output Format
player_id|team_id|jersey_no|name|date_of_birth|age
160140|1207|1|Hugo Lloris|1986-12-26|29
160349|1216|6|Vlad Chiriches|1989-11-14|26
160013|1201|5|Lorik Cana|1983-07-27|32
160467|1221|2|Stephan Lichtsteiner|1984-01-16|32
160401|1218|3|Martin Skrtel|1984-12-15|31
..............
# Task 2
Find the number of games played by each team

# Sample Output Format
team_id|no_of_games
1201|3
1202|3
1203|5
1204|4
1205|3
........
# Task 3
Find the average goal score of each team. The average goal score for a team is the total number of goals divided by the total number of members in the team.

# Sample Output Format
team_id|avg_goal_score
1201|0.0434782608695652
1202|0.0434782608695652
1203|0.391304347826087
1204|0.217391304347826
1205|0.0869565217391304
.......
# Task 4
For each captain find the number of matches he/she has been captain to that match. The result should have captain and no_of_times_captain columns as shown below.

# Sample Output Format
captain|no_of_times_captain
160004|2
160013|1
160028|3
160062|5
160076|4
...........
# Task 5
Find the number of players(no_players) who are captain and also awarded the player of the match for the same match.

# Sample Output Format
no_players
6
# Task 6
Find the distinct player ids who are captain for atleast one match and didn't get the player of the match title for even a single match.

# Sample Output Format
captain
160004
160004
........
# Task 7
Find the number of matches played in each month. Your query should return Month and no_of_matches in the descending order of no_of_matches

# Sample Output Format
month|no_of_matches
06|44
...
# Task 8
Find the jersey number and the number of captains use it. Your query should return jersey_no and no_captains in the descending order of no_captains and jersey_no.

# Sample Output Format
jersey_no|no_captains
1|17
....
# Task 9
Find the average of the audience for each player. In the descending order of avg_audience and player_id.

# Sample Output Format
player_id|avg_audience
160001|49075.66
160002|145675.123
160003|97234.66
160004|72345.852
160005|91203.123
...
# Task 10
Calculate the average age of players for each team.

# Sample Output Format
team_id|AVG(age)
1201|27.0869565217391
1202|27.2173913043478
1203|25.9130434782609
1204|26.304347826087
1205|28.7391304347826
......... 

# Task 11
Calculate the average age of all the captains in the database.

# Sample Output Format
avg_age_of_captains
30.6078431372549	 

# Task 12
Find the month and the number of players born in that month in the descending order of no_of_players and month.

# Sample Output Format
month|no_of_players
01|59
....
# Task 13
Find the captain id and the number of matches he/she has won(no_of_wins). Your Query should return captain and no_of_wins in the descending order of no_of_wins.

# Sample Output Format
captain|no_of_wins
160140|5
160163|4
160322|4
160539|4
160062|3
.........






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
        
