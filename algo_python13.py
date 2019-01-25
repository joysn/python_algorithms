#Input is # of steps in the staircase
#Find out total # of ways in which we can climb the staircase if we vlimb 1 or 2 steps at a time

# no_of_steps = 2
# We can either climb {1,1} or {2}. So the o/p is 2

#####################
### BACK Tracking ###
#####################


## Time Complexity O(2^n) [Binary Tree - n is same as no_of_steps and is same as that of level of the tree]


def move(sum, step,target,count,step_list,possible_steps):
	#print("Called Move with : {} {} {} {} {}".format(sum,step, target, count, possible_steps))
	sum = sum + step
	step_list.append(step)
	#print("New Sum: {}".format(sum))
	#if(count == 4):
	#	exit(0)
	
	if(sum == target):
		count += 1
		print(step_list)
		#print("Count: "+str(count))
		
	if (sum > target):
		#print("Return, sum exceeded "+str(sum))
		step_list.pop()
		return count
		
	if (sum < target):
		for i in possible_steps:
			count = move(sum,i,target,count,step_list,possible_steps)
		
	if step_list:
		step_list.pop()
	return count
	
	
def count_ways(target,possible_steps):
	#print(target)
	sum = 0
	count = 0
	step_list = []
	for i in possible_steps:
		count = move(sum,i,target,count,step_list,possible_steps)
	return count
	

no_of_steps = 2
possible_steps = [1,2]
cnt = count_ways(no_of_steps,possible_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))

possible_steps = [1,2,3]
no_of_steps = 3
cnt = count_ways(no_of_steps,possible_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))

possible_steps = [1,3,5]
no_of_steps = 4
cnt = count_ways(no_of_steps,possible_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))

possible_steps = [1,2]
no_of_steps = 5
cnt = count_ways(no_of_steps,possible_steps)
print("No of ways {} step staircase can be covered with 1,2 steps at a time is {} \n".format(no_of_steps,cnt))


## Output
# (base) D:\>python algo_python13.py
# [1, 1]
# [2]
# No of ways 2 step staircase can be covered with 1,2 steps at a time is 2

# [1, 1, 1]
# [1, 2]
# [2, 1]
# [3]
# No of ways 3 step staircase can be covered with 1,2 steps at a time is 4

# [1, 1, 1, 1]
# [1, 3]
# [3, 1]
# No of ways 4 step staircase can be covered with 1,2 steps at a time is 3

# [1, 1, 1, 1, 1]
# [1, 1, 1, 2]
# [1, 1, 2, 1]
# [1, 2, 1, 1]
# [1, 2, 2]
# [2, 1, 1, 1]
# [2, 1, 2]
# [2, 2, 1]
# No of ways 5 step staircase can be covered with 1,2 steps at a time is 8