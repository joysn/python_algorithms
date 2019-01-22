# Validate Parenthesis In a String

def isOpen(c):
	if c == '{':
		return True
	if c == '(': 
		return True
	if c == '[':
		return True
	else:
		return False
		

def isClose(c):
	if c == '}':
		return True
	if c == ')': 
		return True
	if c == ']':
		return True
	else:
		return False

def findCorresponding(c):
	if c == '}':
		return '{'
	if c == ']':
		return '['
	if c == ')':
		return '('
		
def isValidParenthesis(inp):

	print(inp,end=' :- ')
	myStack = []
	
	i = 0;
	while (i < len(inp)):
		if (isOpen(inp[i])):
			myStack.append(inp[i])
		if (isClose(inp[i])):
			corres = findCorresponding(inp[i])
			if corres != myStack.pop():
				return False
		i = i+1
		
	if len(myStack) != 0:
		return False
	return True
	
print(isValidParenthesis('abc(){()}[]'))
print(isValidParenthesis('({)}'))
print(isValidParenthesis('abc(){()}[]['))

# Output
# (base) D:\>python algo_python8.py
# abc(){()}[] :- True
# ({)} :- False
# abc(){()}[][ :- False
