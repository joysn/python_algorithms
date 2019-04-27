# Given 2 string, find if they match case insenstively

def case_insensitive_compare(s1,s2):
	return s1.upper() == s2.upper()
print("*******************1*******************")
print("True and False")		
print(case_insensitive_compare('abc','ABC'))
print(case_insensitive_compare('abc','ABD'))


#optimization - Given 2 string, find if they match case insenstively
def case_insensitive_compare1(s1,s2):
	if len(s1) != len(s2):
		return False
	s1_iter = iter(s1)
	s2_iter = iter(s2)
	for _ in range(len(s1)):
		s1_c = s1_iter.__next__()
		s2_c = s2_iter.__next__()
		if not s1_c.upper() == s2_c.upper():
			return False
	return True
	
print("*******************2*******************")
print("True, False and False")			
print(case_insensitive_compare1('abc','ABC'))
print(case_insensitive_compare1('abc','ABD'))
print(case_insensitive_compare1('abcd','ABD'))

# Given 2 string, find if they match case insenstively or their distance is 1
def ins_del_compare(s1,s2):
	if len(s1) != len(s2):
		if (abs(len(s1)-len(s2)) == 1):
			shorter,longer = sorted([s1,s2], key = len)
		else:
			return False
	else:
		return case_insensitive_compare1(s1,s2)
		
	shorter_iter = iter(shorter)
	longer_iter = iter(longer)
	for _ in range(len(shorter)):
		shorter_c = shorter_iter.__next__()
		longer_c = longer_iter.__next__()
		if not longer_c.upper() == shorter_c.upper():
			longer_next = longer_iter.__next__()
			if not longer_next.upper() == shorter_c.upper():
				return False
	return True

print("*******************3*******************")
print("True, False and True")	
print(ins_del_compare('abc','ABC'))
print(ins_del_compare('abc','ABD'))
print(ins_del_compare('abcd','ABD'))
	
# Given 2 string, find if they match case insenstively or their distance is n
def editDistance(s1,s2,n,m):
	if n == 0:
		return m
		
	if m == 0:
		return n
		
	if s1[n-1].upper() == s2[m-1].upper():
		return editDistance(s1,s2,n-1,m-1)
	
	return 1 + min(editDistance(s1,s2,n-1,m) # insert
	, editDistance(s1,s2,n,m-1) # delete
	, editDistance(s1,s2,n-1,m-1) # Replace
	)
	
def ins_del_compare2(s1,s2,tolerance):
	
	if abs(len(s1)-len(s2)) > tolerance:
		return False	
	#dynamice program part
	lvdist = editDistance(s1,s2,len(s1), len(s2))
	if lvdist < tolerance:
		return True
	return False

print("*******************4*******************")
print("True, True , True, False, False")	
print(ins_del_compare2('abc','ABC',2))
print(ins_del_compare2('abc','ABD',2))
print(ins_del_compare2('abcd','ABD',2))
print(ins_del_compare2('abcd','ABDef',2))
print(ins_del_compare2('sunday','SATURDAY',2))


# (base) D:\>python algo_python24.py
# *******************1*******************
# True and False
# True
# False
# *******************2*******************
# True, False and False
# True
# False
# False
# *******************3*******************
# True, False and True
# True
# False
# True
# *******************4*******************
# True, True , True, False, False
# True
# True
# True
# False
# False

