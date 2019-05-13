# 0-1 Knapsack
# ● Question: Given a list of items with values and weights, as well as a max weight,
# find the maximum value you can generate from items where the sum of the
# weights is less than the max.
# ● Eg.
# items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
# maxWeight = 5
# knapsack(items, maxWeight) = 22


def ks(n,W):
	global cache
	if cache[n][W]:
		return cache[n][W]
	if n == 0 or W == 0:
		return 0
	elif weights[n] > W:
		result = ks(n-1,W)
	else:
		temp1 = ks(n-1,W)
		temp2 = values[n] + ks(n-1,W-weights[n])
		if temp1 > temp2:
			result = temp1
		else:
			result = temp2
			
	cache[n][W] = result
	return result
	

values = [6, 10, 12] 
weights = [1, 2, 3] 
W = 5
n = len(values) # len = 3, but index ends at 2
cache = [[0 for i in range(W+1)] for j in range(n)]
print(ks(n-1,W)) 	

# (base) D:\>python algo_python17b.py
# 22
