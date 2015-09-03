# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from random import shuffle
no_team=7
with open('../data/students.tsv','rb') as stud_file:
    li=[entry.replace('\t', ' ').replace('\n','') for entry in stud_file]
li=li[1:] #ignore first line of the file

# <codecell>

shuffle(li)
team_size =  len(li)/no_team if len(li)%no_team == 0 else (len(li)/no_team)+1
teams=[li[i:i+team_size] for i in range(0,no_team*team_size,team_size)]

# <codecell>

print "\n".join(str(team) for team in teams)

# <codecell>


