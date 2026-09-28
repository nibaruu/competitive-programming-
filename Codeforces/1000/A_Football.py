a= int(input())
goals=[]
team1=""
team2=""
for _ in range(a):
    team=input()
    goals.append(team)
    if team1=="":
        team1=team
    elif team2==""and team!=team1:
        team2=team 
num=goals.count(team1)
if num>len(goals)/2:
    print(team1)
else:
    print(team2)    

