# Given IDs of players and their strengths, we need to make two teams such that both teams should have equal number of players 
# and total strength of every team should be maximum and the difference between the strengths of both teams should be minimum.
# id = [1 2 3 4]
# strength = [10, 22, 21, 8]
# [1,3] -> 10, 21 (sum of strength = 31)
# [2,4] -> 22,8 (sum of strength = 30)



def DivideTeam(playerIdarr, playerStrengthArr):
	playerDict = dict()
	
	for i in range(0,len(playerIdarr)):
		playerDict[playerStrengthArr[i]] = playerIdarr[i]
		
	#print(playerDict)
	
	#playerSortedDict = dict(sorted(playerDict.items(),reverse=True))
	#print(playerSortedDict)
	
	strength1, strength2 = 0,0
	
	team1, team2 = [], []
	
	for key in sorted(playerDict,reverse=True):
		#print (key, playerDict[key])
		
		if  abs(strength1 + key - strength2) < abs(strength2 + key - strength1):
			strength1 = strength1 + key
			team1.append(playerDict[key])
		else:
			strength2 = strength2 + key
			team2.append(playerDict[key])
		
	print('Strength of Team 1:- ',strength1,' and Team1:- ' ,team1)
	print('Strength of Team 2:- ',strength2,' and Team2:- ' ,team2)
	print('Difference of Strength is: ', abs(strength1 - strength2))
	
	
DivideTeam([1,2,3,4],[10, 22, 21, 8])

# Output
# (base) D:\>python algo_python10.py
# Strength of Team 1:-  31  and Team1:-  [3, 1]
# Strength of Team 2:-  30  and Team2:-  [2, 4]
# Difference of Strength is:  1