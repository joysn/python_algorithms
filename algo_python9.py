# Find the intersection between arrays

def findIntersection(arr1, arr2, arr3):
	output = []
	
	x,y,z = 0,0,0
	
	while  (x < len(arr1)) and (y < len(arr2)) and (z < len(arr3)) :
		if (arr1[x] == arr2[y]) and (arr2[y] == arr3[z]):
			output.append(arr1[x])
			x = x+1
			y = y+1
			z = z+1
		elif arr1[x] < arr2[y]:
			x = x+1
		elif arr2[y] < arr3[z]:
			y = y+1
		else:
			z = z+1
			
	return output
	

arr1 = [2,6,9,11,13,17]
arr2 = [3,6,7,10,13,15]
arr3 = [4,5,6,9,11,13]

print(findIntersection(arr1,arr2,arr3))

# Output
# (base) D:\>python algo_python9.py
# [6, 13]

arr1 = [2,9,11,13,17]
arr2 = [3,6,7,10,13,15]
arr3 = [4,5,6,9,11]

print(findIntersection(arr1,arr2,arr3))

# Output
# []