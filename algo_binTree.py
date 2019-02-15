# Binary Tree

class _BinTreeNode:
	
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
		
	
# Depth First Traversal (DFT), pre-order	
def preorderTrav(subtree):

	if subtree is not None:
		print(subtree.data)
		preorderTrav(subtree.left)
		preorderTrav(subtree.right)
		
# Depth First Traversal (DFT), in-order		
def inorderTrav(subtree):

	if subtree is not None:
		preorderTrav(subtree.left)
		print(subtree.data)
		preorderTrav(subtree.right)
		
		
# Depth First Traversal (DFT), post-order
def postorderTrav(subtree):

	if subtree is not None:
		preorderTrav(subtree.left)
		preorderTrav(subtree.right)
		print(subtree.data)
		
# Breadth First Traversal (BFT)
def breadthFirstTraversal(bintree):
	Queue q
	q.enqueue(bintree)
	
	while not q.isEmpty():
		node = q.dequeue()
		print(node.data)
		
		if node.left is not None:
			q.enqueue(node.left)
		if node.right is not None:
			q.enqueue(node.right)
	
	
#################
# Expression Tree
#################

class _ExpTreeNode:
	def __init__(self,data):
		self.element = data
		self.left = None
		self.right = None
		
class ExpressionTree:
	
	def __init__(self,expStr):
		self._expTree = None
		self._buildTree(expStr)
		
	def evaluate(self, varMap):
		return self._evalTree(self._expTree,varMap)
		
	def __str__(self):
		return self.__buildString(self._expTree)
		
		
	''' retruns the element if it is a leaf
	    returns { left op right } it not '''
	def __buildString(self, treeNode):
		if (treeNode.left == None) && (treeNode.right == None):
			return treeNode.element
		else:
			str = '';
			str+= '('
			str += self.__buildString(treeNone.left)
			str += treeNode.element
			str += self.__buildString(treeNone.right)
			str += '}'
			return str
			
			
	def __evalTree(self, treeNode, varDict):
		
		if (treeNode.left == None) && (treeNode.right == None):
			if treeNode.element >= '0' and treeNode.element <= '9':
				return int(treeNode.element)
			else: # variable
				assert treeNode.element in varDict, "Invalid Variab;e"
				return varDict[treeNode.element]
				
		else: # An operator
			lvalue = __evalTree(treeNode.left, varDict)
			rvalue = __evalTree(treeNode.right, varDict)
			return _computeOp(lvalue, treeNode.element, rvalue)
			
	def __computeOp(left, op, right):
		if op == '+':
			return int(left) + int(right)
		elif op == '-':
			return int(left) - int(right)
		elif op == '*':
			return int(left) * int(right)
		elif op == '/':
			return int(left) / int(right)
		elif op == '%':
			return int(left) % int(right)
		else:
			assert 1=1, "incorrect operand"
			
	def __buildTree(self, expStr):
	
		expQ = Queue()
		for token in expStr:
			expQ.enqueue()
			
		self._expTree = __expTreeNode(None)
		self._recBuildTree(self._expTree,expQ)
		
		
	def _recBuildTree(self,currNode, expQ):
	
		token = expQ.dequeue()		
		if token == '(':
			currNode.left = _ExpTreeNode(None)
			self._recBuildTree(currNode.left, expQ)
			
			currNode.element = expQ.dequeue()
			
			currNode.right = _ExpTreeNode(None)
			self._recBuildTree(currNode.right, expQ)
			
			expQ.dequeue()
			
		else:
			currNode.element = token
		
			
		