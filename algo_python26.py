#s: abbc
#b: cbabadcbbabbcbabaabccbabc
# Example: Given a smaller string 5 and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation.


def find_perm1(s,b):
	for i in range(0,len(b)): #O(b)
		temp = b[i:i+len(s)]
		#print(temp)
		if sorted(list(temp)) == sorted(list(s)): #O(s*log(s))
			print(temp+' at '+str(i))
				

find_perm1('abbc','cbabadcbbabbcbabaabccbabc') #O(b * s*log(s))

# (base) D:\>python algo_python26.py
# cbab at 0
# cbba at 6
# abbc at 9
# bcba at 11
# cbab at 12
# cbab at 20
# babc at 21

## *********************************************************************************
## Enhancement - Use anagram function which finds if it is anagram or not in O(s) **
## *********************************************************************************

debug = False
def isanagram(s1,s2):
	# Not required in this case we have both the strings of same size
	if len(s1) != len(s2):
		print('{} {} Is Not Anagram'.format(s1,s2)) if debug else None
		return False
	else:
		s1 = s1.lower()
		s2 = s2.lower()
		s1_dict = {}
		for i in range(0,len(s1)):
			if s1[i] in s1_dict.keys():
				s1_dict[s1[i]] = s1_dict[s1[i]]+1
			else:
				s1_dict[s1[i]] = 1
		#print(s1_dict) 
		
		for i in range(0,len(s2)):
			if s2[i] not in s1_dict.keys():
				print('{} {} Is Not Anagram'.format(s1,s2)) if debug else None
				return False
			else:
				s1_dict[s2[i]] = s1_dict[s2[i]] -1
				
		for key in s1_dict.keys():
			if s1_dict[key] != 0:
				print('{} {} Is Not Anagram'.format(s1,s2)) if debug else None
				return False
		print('{} {} Is Anagram'.format(s1,s2)) if debug else None
		return True

# Testing Anagram		
#isanagram('abc','bac')
#isanagram('abc','ba')
#isanagram('abc','bab')
#isanagram('abc','bad')
#isanagram('abc','BAC')
#isanagram('aBc','bac')
#isanagram('','')

print('****************************')

def find_perm2(s,b):
	for i in range(0,len(b)): #O(b)
		temp = b[i:i+len(s)]
		#print(temp)
		if isanagram(temp,s): #O(s))
			print(temp+' at '+str(i))
			
find_perm2('abbc','cbabadcbbabbcbabaabccbabc') #O(b * s))


#(base) D:\>python algo_python26.py
# cbab at 0
# cbba at 6
# abbc at 9
# bcba at 11
# cbab at 12
# cbab at 20
# babc at 21

print('****************************')

## ******************************************************************
## Enhancement - Refine anagram functions to reduce some more work **
## ******************************************************************

def isanagram2(s1,**s_dict):
	# Not required in this case we have both the strings of same size
	#if len(s1) != len(s2):
	#	print('{} {} Is Not Anagram'.format(s1,s2)) if debug else None
	#	return False
	#else:
		#s1 = s1.lower() # Not required
		#s2 = s2.lower() # Not required
		
		# Not required since we are getting it
		# s1_dict = {}
		# for i in range(0,len(s1)):
			# if s1[i] in s1_dict.keys():
				# s1_dict[s1[i]] = s1_dict[s1[i]]+1
			# else:
				# s1_dict[s1[i]] = 1
		#print(s_dict)
		s_dict_temp = s_dict
		for i in range(0,len(s1)):
			if s1[i] not in s_dict_temp.keys():
				print('{} {} Is Not Anagram'.format(s1,s_dict)) if debug else None
				return False
			else:
				s_dict_temp[s1[i]] = s_dict_temp[s1[i]] -1
				
		for key in s_dict_temp.keys():
			if s_dict_temp[key] != 0:
				print('{} {} Is Not Anagram'.format(s1,s_dict)) if debug else None
				return False
		print('{} {} Is Anagram'.format(s1,s_dict)) if debug else None
		return True
		
def find_perm3(s,b):

	s_dict = {}
	s = s.lower()
	b = b.lower()
	for i in range(0,len(s)): #O(s)
		if s[i] not in s_dict.keys():
			s_dict[s[i]] = 1
		else:
			s_dict[s[i]] = s_dict[s[i]] + 1
			
	cnt1 = 0
	cnt2 = 0
	cnt3 = 0
	for i in range(0,len(b)-len(s)+1): #O(b-s)
		cnt1 += 1
		skip = False
		for j in range(i,i+len(s)):
			#print(i,j)
			if b[j] not in s_dict.keys():
				i = j+1
				skip = True
		if skip == True:
			continue
		cnt2 += 1
		temp = b[i:i+len(s)]
		#print(temp)
		if isanagram2(temp,**s_dict): #O(s)
			print(temp+' at '+str(i))
	print(cnt1,cnt2)
	print("The count is {} {}".format(cnt1,cnt2)) if debug else False
	
	
find_perm3('abbc','cbabadcbbabbcbabaabccbabc') #O(b-s * s))



print('****************************')