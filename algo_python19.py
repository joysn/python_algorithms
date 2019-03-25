# Given a list of numbers,remove and print every third number from a list of numbers until the list becomes empty.

# Input : [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Output : 30 60 90 40 80 50 20 70 10
# Explanation:
# The first third element encountered is 30, after 30 we start the count from 40 for the next third element which is 60, after that 90 is encountered. Then again the count starts from 10 for the next third element which is 40. Proceeding in the same manner as we did before we get next third element after 40 is 80. This process is repeated until the list becomes empty.

# Input : [1, 2, 3, 4]
# Output : 3 2 4 1
# Explanation:
# The first third element encountered is 3, after 3 we start the count from 4 for the next third element which is 2. Then again the count starts from 4 for the next third element which is 4 itself and finally the last element 1 is printed.


def get_next_pos(start, nth, length):
	ele_to_rem = start + nth - 1;
	if ele_to_rem > length:
		ele_to_rem = (start + nth) % length -1 
		if ele_to_rem == -1:
			ele_to_rem = length - 1
			
	return ele_to_rem
	
if __name__ == '__main__':

	debug = False
	
	ar = [1,2,3,4]
	ar = [10, 20, 30, 40, 50, 60, 70, 80, 90]
	op = []
	nth = 3

	print("Given Array ",ar) if debug else None
	
	start = 0
	length = len(ar)	
	op_idx = 0
	
	while (length != 0):
		print("Start ", start, " nth ", nth, " length ",length) if debug else None
		ele_to_rem = get_next_pos(start,nth,length)
		op.append([])
		print("Array before removal of ",ele_to_rem, " position element is ",ar) if debug else None
		op[op_idx] = ar.pop(ele_to_rem)
		print("Element removed                                 ",op[op_idx]) if debug else None
		print("Array after removal                             ",ar) if debug else None
		op_idx += 1
		start = ele_to_rem
		length = len(ar)

	print(op)

	
# (base) D:\>python algo_python19.py
# [3, 2, 4, 1]

# (base) D:\>python algo_python19.py
# [30, 60, 90, 40, 80, 50, 20, 70, 10]