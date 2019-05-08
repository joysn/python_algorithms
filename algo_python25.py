# This code counts all permutations of a string.

cnt1 = 0
cnt2 = 0

def permutations(str,prefix):
	global cnt1,cnt2
	if len(str) == 0:
		cnt2 = cnt2+1 ## n! times * n [n is cost of printing the string]
		print(prefix)
	else:
		for i in range(0,len(str)):
			cnt1 = cnt1+1
			print("Intermediate "+str+" "+prefix)
			rem = str[0:i] + str[i+1:]
			permutations(rem, prefix+str[i:i+1])	## n! times permutations is called at the last level. There is tree above it. So O(n*n!)
	
permutations('abc','')
print(cnt1,cnt2)
# total time complexity is O(n*n! + n*n!) ~ O(n*n!)