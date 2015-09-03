# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from random import shuffle
no_team=6
with open('../data/students.tsv','rb') as stud_file:
    li=[entry.replace('\t', ' ').replace('\n','') for entry in stud_file]
li=li[1:] #ignore first line of the file

# <codecell>

shuffle(li)
team_size =  len(li)/no_team
teams=[li[i:i+team_size] for i in range(0,team_size*no_team,team_size)]
for i in range(team_size*no_team, len(li)):
    teams[i-team_size*no_team].append(li[i])

# <codecell>

print "\n".join(str(team) for team in teams)

# <codecell>


