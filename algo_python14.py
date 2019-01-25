#Input is # of steps in the staircase
#Find out total # of ways in which we can climb the staircase if we vlimb 1 or 2 steps at a time

# no_of_steps = 2
# We can either climb {1,1} or {2}. So the o/p is 2

###########################
### Dynamic Programming ###
###  Top Down Approach  ###
###      Caching        ###
###########################

## Time Complexity O(n) [Due to ]

def count_ways(target):
	global cache
	cnt = 0
	if target == 0:
		return 1
	elif target < 0:
		return 0
	elif target in cache:
		return cache[target]
	else:
		global possible_steps
		for i in possible_steps:
			cnt = cnt + count_ways(target-i)
	if not target in cache:
		cache[target] = cnt
	return cnt
	

	
cache = {}
no_of_steps = 2
possible_steps = [1,2]
cnt = count_ways(no_of_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))
#print(cache)

cache = {}
possible_steps = [1,2,3]
no_of_steps = 3
cnt = count_ways(no_of_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))

cache = {}
possible_steps = [1,3,5]
no_of_steps = 4
cnt = count_ways(no_of_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))

cache = {}
possible_steps = [1,2]
no_of_steps = 5
cnt = count_ways(no_of_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))

## Output
# (base) D:\>python algo_python14.py
# No of ways 2 step staircase can be covered with 1,2 steps at a time is 2

# No of ways 3 step staircase can be covered with 1,2 steps at a time is 4

# No of ways 4 step staircase can be covered with 1,2 steps at a time is 3

# No of ways 5 step staircase can be covered with 1,2 steps at a time is 8