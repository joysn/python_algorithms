# Unbound knapsack
# Python3 program to find maximum achievable value with a knapsack of weight max_weight and multiple instances allowed. 
# Returns the maximum value  with knapsack of max_weight capacity 

def unboundedKnapsack(max_weight, values, weights): 
  
    # sack[wt] is going to store maximum  value with knapsack capacity wt. 
    sack = [0 for i in range(max_weight + 1)] 
  
    ans = 0
  
    # Fill sack[] using above recursive formula 
    for wt in range(max_weight + 1): 
        for j in range(len(values)): 
            if (weights[j] <= wt): 
                sack[wt] = max(sack[wt], sack[wt - weights[j]] + values[j]) 
  
    return sack[max_weight] 
  
max_weight = 100
values = [10, 30, 20] 
weights = [5, 10, 15]  
  
print(unboundedKnapsack(max_weight, values, weights)) 

# (base) D:\>python algo_python17b.py
# 300