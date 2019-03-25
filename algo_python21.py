# Given a list of lists, the task is to find the elements which are common in all sublist.
# Python code to find duplicate element in all  
# sublist from list of list 
  
# List of list initialization 
Input = [ [10, 20, 30, 40], 
          [30, 40, 60, 70], 
          [20, 30, 40, 60, 70], 
          [30, 40, 80, 90], ] 
		  

op = set(Input[0])
for l in Input[1:]:
	op &= set(l)
	
print(list(op))

# Given a list, print all the sublists of a list.
# Input  : list = [1, 2, 3] 
# Output : [[], [1], [1, 2], [1, 2, 3], [2], 
         # [2, 3], [3]]


def sub_lists(l1):
	
	op = []
	op.append([])
	for i in range(len(l1)):
		for j in range(i+1,len(l1)+1):
			sub = l1[i:j]
			op.append(sub)
			print(i,j)
			
	return op

if __name__ == '__main__':		 
	l1 = [1, 2, 3] 
	print(sub_lists(l1)) 
	
# (base) D:\>python algo_python21.py
# [[], [1], [1, 2], [2]]



# Given a list of lists, write a Python program to count the number of sublists containing the given 

def countList(lst, x):
	count = 0
	for ele in lst:
		if x in ele:
			count += 1
	return count
	
lst = (['a'], ['a', 'c', 'b'], ['d'])  
x = 'a'
print(countList(lst, x))
# (base) D:\>python algo_python21.py
# 2



Input = [['Machine', 'London', 'Canada', 'France', 'Lanka'], 
         ['Spain', 'Munich'], 
         ['Australia', 'Mandi']] 
		 
sort_l = []
for l in Input:
	l.sort()
	sort_l.append(l)
	
print(sort_l)

# (base) D:\>python algo_python21.py
# [['Canada', 'France', 'Lanka', 'London', 'Machine'], ['Munich', 'Spain'], ['Australia', 'Mandi']]