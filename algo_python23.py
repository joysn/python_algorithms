## Give a wallet amount and the item cost, find the max amount of items that can be bought from the wallet_amount

def knapsack(amount):

	global cache
	global allowed_items
	
	value = 0
	max_value = 0
	
	if amount == 0:
		return max_value
		
	if amount in cache:
		return cache[amount]
		
	for i in range(0,len(allowed_items)):
		if amount - allowed_items[i] >= 0:
			#print("Value and Weight",value,weight - weights[i])
			value = allowed_items[i] + knapsack(amount - allowed_items[i])
			if value > max_value:
				max_value = value
				#print("Max Value ",max_value)
	
	if amount not in cache:
		cache[amount] = value
	return max_value

	

cache = {}
allowed_items = [18,21]
wallet_amount = 61
max_value = 0
print(knapsack(wallet_amount))



def unboundedKnapsack1():

	global wallet_amount
	global allowed_items
	
	sack = [0 for i in range(wallet_amount+1)]

	for amount in range(wallet_amount+1):
		for item in allowed_items:
			if item < amount:
				sack[amount] = max(sack[amount], sack[amount-item]+item)

	return sack[wallet_amount]
	
wallet_amount = 457
allowed_items = [19,21]  
print(unboundedKnapsack1()) 