# practice 1
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests
from pprint import pprint   

def getScore(total_page,base_url,total_score,team):
    for page in range(1,total_page+1):
        curr_url = base_url+str(page)
        res = requests.get(curr_url)
        json_res = res.json()
        data = json_res['data']
        for each_data in data:
            total_score += int(each_data[team])
    return total_score
    

def getTotalGoals(team, year):
    home_team_url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) +"&team1="+ team+"&page=1"
    home_team_base_url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) +"&team1="+ team+"&page="
    away_team_url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) +"&team2="+ team+"&page=1"
    away_team_base_url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) +"&team2="+ team+"&page="
    r_home = requests.get(home_team_url)
    r_away = requests.get(away_team_url)
    json_res_home = r_home.json()
    json_res_away = r_away.json()
    total_page_as_home = json_res_home['total_pages']
    total_page_as_away = json_res_away['total_pages']
    
    home_score = getScore(total_page_as_home,home_team_base_url,0,'team1goals')
    away_score = getScore(total_page_as_away,away_team_base_url,0,'team2goals')
    total_score = home_score + away_score 
    return total_score



    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
