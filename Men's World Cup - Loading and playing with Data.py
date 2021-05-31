#!/usr/bin/env python
# coding: utf-8

# # ⚽⚽ Playing with Statsbomb data ⚽⚽
# 
# 🎊 Using Statsbomb to load World Cup 2018 data. Let's see what can we do with this data 🎊
# 
# ### What are we doing here?
# 
# Let's Use some StatsBomb data for World Cup 2018 and find something interesting!
# 
# ### DATA
# 
# We will be use the <a href='https://github.com/statsbomb/open-data'>StatsBomb open-data</a> from Github to work on.

# In[1]:


# Imports
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from pandas import json_normalize
# from matplotlib.patches import Arc
from mplsoccer import Pitch
from FCPython import createPitch

# In[0]:
    
# ## ⚽Getting the data ready
# 
# Using json library, lets get the data ready.

# In[2]:


# Now lets set the competition id manually
# Men's International World Cup has competition id = 43

competition_id = 43


# In[3]:


# Now lets load the competitions json file
with open('statsbomb/data/competitions.json') as f:
    competitions = json.load(f)
    
competitions[0]


# In[4]:


# Now let's get the matches for competition 43
location=os.listdir('statsbomb/data/matches/'+str(competition_id)+'/')
for i in location:
    filename=i
    break
with open('statsbomb/data/matches/'+str(competition_id)+'/'+filename) as f:
    matches = json.load(f)
    
matches[0]


# ## ⚽Visualising the Matche Results :
# Let's create a function that will:
# 1. Display all the matches
# 2. Display in a grid of 5 per row
# 3. visualise the goals scored by each team

# In[5]:


def show_25_matches(home_teams, away_teams, home_scores, away_scores):
    '''
    Function to display the results(goals) of 25 World Cup matches
    '''
    plt.figure(figsize=(15,15))
    for i in range(25):
        ax = plt.subplot(5,5,i+1)
        plt.title(home_teams[i]+' vs '+away_teams[i])
        plt.ylim(bottom=1)
        plt.yticks([0,1,2,3,4,5])
        if home_scores[i]<away_scores[i]:
            colors=['r','g']
        elif home_scores[i]>away_scores[i]:
            colors=['g','r']
        else:
            colors=['b','b']
        plt.bar([home_teams[i],away_teams[i]],
                [home_scores[i],away_scores[i]],
                color=colors)
        if home_scores[i]<away_scores[i]:
            ax.get_xticklabels()[0].set_color("red")
            ax.get_xticklabels()[1].set_color("green")
        elif home_scores[i]>away_scores[i]:
            ax.get_xticklabels()[0].set_color("green")
            ax.get_xticklabels()[1].set_color("red")
        else:
            ax.get_xticklabels()[0].set_color("blue")
            ax.get_xticklabels()[1].set_color("blue")
        plt.tight_layout()

def show_matches(home_teams, away_teams,
                 home_scores, away_scores, figwid=15, fighgt=30):
    '''
    Function to display the results(goals) of all World Cup matches
    '''
    plt.figure(figsize=(figwid,fighgt))
    size=len(home_teams)
    rows=int(np.ceil(size/5))
    for i in range(size):
        ax = plt.subplot(rows,5,i+1)
        plt.title(home_teams[i]+' vs '+away_teams[i])
        plt.ylim(bottom=1)
        plt.yticks([0,1,2,3,4,5])
        if home_scores[i]<away_scores[i]:
            colors=['r','g']
        elif home_scores[i]>away_scores[i]:
            colors=['g','r']
        else:
            colors=['b','b']
        plt.bar([home_teams[i],away_teams[i]],
                [home_scores[i],away_scores[i]],
                color=colors)
        if home_scores[i]<away_scores[i]:
            ax.get_xticklabels()[0].set_color("red")
            ax.get_xticklabels()[1].set_color("green")
        elif home_scores[i]>away_scores[i]:
            ax.get_xticklabels()[0].set_color("green")
            ax.get_xticklabels()[1].set_color("red")
        else:
            ax.get_xticklabels()[0].set_color("blue")
            ax.get_xticklabels()[1].set_color("blue")
        plt.tight_layout()


# In[6]:


# Let's check each match details
home_teams, away_teams, home_scores, away_scores=[],[],[],[]
for match in matches:
    home_team_name = match['home_team']['home_team_name']
    away_team_name = match['away_team']['away_team_name']
    home_score = match['home_score']
    away_score = match['away_score']
    home_teams.append(home_team_name)
    away_teams.append(away_team_name)
    home_scores.append(home_score)
    away_scores.append(away_score)
show_25_matches(home_teams, away_teams, home_scores, away_scores);
# show_matches(home_teams, away_teams, home_scores, away_scores) ##All Matches


# ## ⚽Country Specific match results
# 
# Lets find country specific match results. PFB the countries that competed in the World Cup 2018
# 
# ['Croatia', 'Nigeria', 'Poland', 'Croatia', 'Brazil', 'Germany', 'Australia', 'Serbia', 'Senegal', 'Panama', 'Switzerland', 'France', 'Uruguay', 'Brazil', 'Russia', 'Denmark', 'Costa Rica', 'France', 'Belgium', 'Belgium', 'Argentina', 'France', 'Brazil', 'Uruguay', 'France', 'Iceland', 'Poland', 'Denmark', 'Egypt', 'Argentina', 'Spain', 'Belgium', 'Peru', 'Uruguay', 'South Korea', 'Spain', 'Brazil', 'Nigeria', 'Japan', 'Saudi Arabia', 'Uruguay', 'Japan', 'Morocco', 'Iran', 'Russia', 'Sweden', 'Portugal', 'Portugal', 'Mexico', 'Iran', 'England', 'England', 'Colombia', 'Sweden', 'Croatia', 'Sweden', 'South Korea', 'Colombia', 'France', 'Belgium', 'Russia', 'Germany', 'Serbia', 'Tunisia']

# In[7]:


# Manually input the country you are interested
country='Argentina'

# Let's check country specific match details
home_teams, away_teams, home_scores, away_scores=[],[],[],[]
for match in matches:
    home_team_name = match['home_team']['home_team_name']
    away_team_name = match['away_team']['away_team_name']
    if home_team_name==country or away_team_name==country:
        home_score = match['home_score']
        away_score = match['away_score']
        home_teams.append(home_team_name)
        away_teams.append(away_team_name)
        home_scores.append(home_score)
        away_scores.append(away_score)
show_matches(home_teams, away_teams, home_scores, away_scores, figwid=10,fighgt=5) ##All Matches


# ## ⚽ Matchup between 2 countries
# 
# Pick any Two teams and lets see the scores between them. 
# * If the match happened, we can visualise the data as well.
# * If the match didnt happen, lets check the other teams.

# In[8]:


# Let us create a funtion that will output the match ids
def match_id(team1, team2):
    '''
    With team1 and team2 as input the output will the match ids of the two teams.
    '''
    ids=[]
    flag=0
    for match in matches:
        home_team_name = match['home_team']['home_team_name']
        away_team_name = match['away_team']['away_team_name']
        if (home_team_name==team1 or away_team_name==team1) and (home_team_name==team2 or away_team_name==team2):
            ids.append(match['match_id'])
            flag=1
    return ids,flag        


# In[9]:


# Let's input the 2 teams
team1='Argentina'
team2='Croatia'

# Get the match id
match_ids,flag = match_id(team1,team2)
if flag:
    print('The Match id(s) are: '+str(match_ids))
else:
    print('The mentioned teams didnt match up in the group stage.')


# ## ⚽Event based Visualisation: Pass Maps
# 
# Now let's use the Match ids to explore some event based visuals such as the passing maps and more...

# In[10]:


# Some constants to use..

# Argentina vs Croatia match id
match_id_required=7545

# Pitch lengths in yards
pitchLengthX=128
pitchWidthY=80


# In[11]:


# Loading the Match data using the match_id
filename = 'statsbomb/data/events/'+str(match_id_required)+'.json'
# print(filename)
with open(filename,encoding='utf-8') as f:
    data=json.load(f)
data


# In[12]:


# Now creating a DataFrame and Storing the DataFrame in a dictionary with match id as Key
df = json_normalize(data, sep='_').assign(match_id=filename[-9:-5])


# In[13]:


# A dataframe of only Shots
shots = df[df['type_name']=='Shot'].set_index('id')
shots.head()


# In[15]:


# fig,ax = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
pitch = Pitch(pitch_type='custom',  # example plotting a tracab pitch
              pitch_length=pitchLengthX, pitch_width=pitchWidthY,
              axis=True, label=True)  # showing axis labels is optional
fig, ax = pitch.draw(figsize=(16, 11),
                      constrained_layout=False,
                      tight_layout=True)

# Now lets plot the shots
for i,shot in shots.iterrows():
    x=shot['location'][0]
    y=shot['location'][1]
    goal=shot['shot_outcome_name']=='Goal'
    team_name=shot['team_name']
    
    circleSize=2
    #circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12
    if (team_name==team1):
        if goal:
            # shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            shotCircle=pitch.scatter(x, 
                                     pitchWidthY-y,
                                     marker='football',
                                     ax=ax)
            # plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
        else:
            shotCircle=pitch.scatter(x, pitchWidthY-y, ax=ax)
            # shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
    elif (team_name==team2):
        if goal:
            shotCircle=pitch.scatter(pitchLengthX-x,
                                     y,
                                     marker='football',
                                     ax=ax)
            # shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
            # plt.text((pitchLengthX-x+1),y+1,shot['player_name']) 
        else:
            shotCircle=pitch.scatter(pitchLengthX-x, y, ax=ax)
            # shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")
    # ax.add_patch(shotCircle)

    
# plt.text(5,75,team2 + ' shots') 
# plt.text(80,75,team1 + ' shots') 
     
# fig.set_size_inches(10, 7)
# fig.savefig('statsbomb/outputs/shots.pdf', dpi=100) 
plt.show()

# In[ ]:

(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

#Plot the shots
for i,shot in shots.iterrows():
    x=shot['location'][0]
    y=shot['location'][1]
    
    goal=shot['shot_outcome_name']=='Goal'
    team_name=shot['team_name']
    
    circleSize=2
    #circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12

    if (team_name==team1):
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.2)
    elif (team_name==team2):
        if goal:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
            plt.text((pitchLengthX-x+1),y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")      
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)
    
    
plt.text(5,75,team2 + ' shots') 
plt.text(80,75,team1 + ' shots') 
     
fig.set_size_inches(16, 11)
# fig.savefig('Output/shots.pdf', dpi=100) 
plt.show();



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




