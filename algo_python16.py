# Make change using the coins [25,10,5,1] using minimum number of coins
# Dynamic Programming, Top Down approach

def makeChange(c):
	global coins
	global change
	
	if c == 0:
		return 1
	if c < 0:
		change.pop()
		return 0
	if c > 0:
		for i in coins:
			change.append(i)
			if (makeChange(c-i)):
				return 1
	

coins = [25,10,5,1]

change = []
makeChange(1)
print(change)

change = []
makeChange(6)
print(change)

change = []
makeChange(10)
print(change)

change = []
makeChange(49)
print(change)


# Output
# (base) D:\>python algo_python16.py
# [1]
# [5, 1]
# [10]
# [25, 10, 10, 1, 1, 1, 1]