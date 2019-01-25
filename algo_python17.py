# Knapsack

# Given a list of items with values and weights, as well as a max
# weight, find the maximum value you can generate from items,
# where the sum of the weights is less than or equal to the max.
# items = {(w:2, v:6), (w:2, v:10), (w:3, v:12)}
# max weight = 5
# knapsack(items, max weight) = 22

##Dynamic Programming, top down, Time = O(n), space = O(n)

 
 
def knapsack(weight):
	global cache
	curr_value = 0
	max_value = 0
	
	if weight == 0:
		return max_value
	
	
	if weight in cache:
		return cache[weight]
		
	for i in range(0,len(weights)):
		#print(weights[i],values[i])
		
		if weight - weights[i] >= 0:
			curr_value = values[i]
			curr_value += knapsack(weight - weights[i])
			if curr_value > max_value:
				max_value = curr_value
			
	if not weight in cache:
		cache[weight] = max_value
	return max_value
	

weights = [2,2,3]
values = [6,10,12]

input = [0,1,2,3,4,5,6]
for i in input:
	cache = {}
	max_weight = i
	mvalue = knapsack(max_weight)
	print("Max value of {} can be put with max of {} ".format(mvalue,max_weight))

# Output
# (base) D:\>python algo_python17.py
# Max value of 0 can be put with max of 0
# Max value of 0 can be put with max of 1
# Max value of 10 can be put with max of 2
# Max value of 12 can be put with max of 3
# Max value of 20 can be put with max of 4
# Max value of 22 can be put with max of 5
# Max value of 30 can be put with max of 6


