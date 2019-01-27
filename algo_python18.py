# Knapsack

# Given a list of items with values and weights, as well as a max
# weight, find the maximum value you can generate from items,
# where the sum of the weights is less than or equal to the max.
# items = {(w:2, v:6), (w:2, v:10), (w:3, v:12)}
# max weight = 5
# knapsack(items, max weight) = 22

##Dynamic Programming, bottom up, Time = O(n), space = O(n)

 
 
def knapsack(weight):
	global cache
	global weights
	global values
	
	cache[0] = 0

	if weight > 0:
		for i in range(1,weight+1):
			max_val = 0
			for j in range(0, len(weights)):
				if (i - weights[j]) >= 0:
					temp_val = values[j] + cache[i-weights[j]]
					if temp_val > max_val:
						max_val = temp_val
			cache[i] = max_val
	
	
	#print(cache)
	return cache[weight]

weights = [2,2,3]
values = [6,10,12]

	
input = [0,1,2,3,4,5,6]
for i in input:
	cache = {}
	max_weight = i
	mvalue = knapsack(max_weight)
	print("Max value of {} can be put with max of {} ".format(mvalue,max_weight))

# cache = {}
# max_weight = 100
# mvalue = knapsack(max_weight)
# print("Max value of {} can be put with max of {} ".format(mvalue,max_weight))


# Output
# (base) D:\>python algo_python18.py
# Max value of 0 can be put with max of 0
# Max value of 0 can be put with max of 1
# Max value of 10 can be put with max of 2
# Max value of 12 can be put with max of 3
# Max value of 20 can be put with max of 4
# Max value of 22 can be put with max of 5
# Max value of 30 can be put with max of 6
