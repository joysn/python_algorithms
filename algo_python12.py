# Place n queeens in n*n board such that each of them are safe

queens = []

def isSafe(r,c):
	#print("Input to isSafe: ",queens, r, c)
	for i in range(0, len(queens)-1):
		if queens[i][0] == r:
			#print("isSafe: False")
			return False
		if abs(queens[i][0] - r) == abs(queens[i][1]-c):
			#print("isSafe: False")
			return False
	#print("isSafe: True")
	return True

def placeQueens(col,n):

	if col >= n:
		return True
	row = 0
	while row < n:
		queens.append([row,col])
		#print("Pushing: ", row,col)
		if (isSafe(row,col)) and (placeQueens(col+1,n)):
			return True
		queens.pop()
		#print("Popping: ", row,col)
		row = row + 1
	return False
	

def nQueens(n):
	if n <= 0:
		return null
		
	if placeQueens(0,n):
		return queens
	else:
		return False
		
		
print(nQueens(5))