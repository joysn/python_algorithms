# Ways to remove duplicates from list

test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 

op = []
for i in test_list:
	if i not in op:
		op.append(i)
		
print(op)

op1 = []
[op1.append(i) for i in test_list if i not in op1]
print(op1)

# (base) D:\>python algo_python20.py
# The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
# [1, 3, 5, 6]
# [1, 3, 5, 6]

# Given a list of strings, write a Python program to remove all digits from the list of string.
# Examples:
# Input : ['alice1', 'bob2', 'cara3']
# Output : ['alice', 'bob', 'cara']
# Input : ['4geeks', '3for', '4geeks']
# Output : ['geeks', 'for', 'geeks']


list = ['4geeks', '3for', '4geeks'] 
list = ['alice1', 'bob2', 'cara3']
op_list = []
for ele in list:
	newele = ""
	for char in ele:
		if not char.isdigit():
			newele += char
			
	op_list.append(newele)
	
print(op_list)

# (base) D:\>python algo_python20.py
# ['geeks', 'for', 'geeks']

# (base) D:\>python algo_python20.py
# ['alice', 'bob', 'cara']



# Python3 code to demonstrate 
# remove last character from list of strings 
# using list comprehension + list slicing   
# initializing list 
test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils'] 

op_list = []
for ele in test_list:
	newele = ele[:-1]
	#print(newele)
	op_list.append(newele)
	
print(op_list)

# (base) D:\>python algo_python20.py
# ['Manjeet', 'Akash', 'Akshat', 'Nikhil']


# Python | Remove empty tuples from a list
# Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  # ('krishna', 'akbar', '45'), ('',''),()]
# Output : [('ram', '15', '8'), ('laxman', 'sita'), 
          # ('krishna', 'akbar', '45'), ('', '')]
		  
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 
		  
tuples = [t for t in tuples if t]
print(tuples)