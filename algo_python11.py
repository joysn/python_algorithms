# Given a chessboard, how would you find whether a king is threatened by the queen or not.
#   1 2 3 4 5 6 7 8
#   - - - - - - - - 
#1 |*     *     *  |
#2 |  *   *   *    |
#3 |    * * *      |
#4 |* * * K * * * *|
#5 |    * * *      |
#6 |  *   *   *    |
#7 |*     *     *  |
#8 |      *       *|
#   - - - - - - - - 


def isThreatened(queenX, queenY, kingX, kingY):
	if (queenX == kingX) or (queenY == kingY) or (abs(queenX - kingX) == abs(queenY - kingY)):
		return 'Threatended'
	else:
		return 'Not Threatended'
		

print(isThreatened(2,4,4,4))
print(isThreatened(4,8,4,4))
print(isThreatened(1,1,4,4))
print(isThreatened(8,8,4,4))
print(isThreatened(5,3,4,4))
print(isThreatened(6,2,4,4))


print(isThreatened(2,5,4,4))
print(isThreatened(5,8,4,4))
print(isThreatened(3,1,4,4))
print(isThreatened(7,8,4,4))
print(isThreatened(6,3,4,4))
print(isThreatened(7,2,4,4))

# Output
# (base) D:\>python algo_python11.py
# Threatended
# Threatended
# Threatended
# Threatended
# Threatended
# Threatended
# Not Threatended
# Not Threatended
# Not Threatended
# Not Threatended
# Not Threatended
# Not Threatended
