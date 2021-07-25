import torch

# Example taken from first few lines of https://people.sc.fsu.edu/~jburkardt/data/cnf/aim-50-1_6-yes1-4.cnf
## Main source: https://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.htm
# a b d 0
# -b c d 0
# -b -c d 0
A = [[1,1,0,1,0],
	 [0,-1,1,1,1],
	 [0,-1,-1,1,2],
	 [1,0,0,0,0],
	 [0,0,0,0,1]]
A = [[1,1,0,1,0],
	 [0,-1,1,1,1],
	 [0,-1,-1,1,2],
	 [0,0,0,-1,1],
	 [0,0,0,0,1]]
A = [[1,0,0,0],
	 [0,1,0,0],
	 [0,0,1,0],
	 [1,1,1,1]]
# B = [[1],[1],[1]]
def is_decimal(tensor):
	if(torch.all(tensor.long()==tensor)):
		return False
	else:
		return True
A = torch.Tensor(A)

# C = [[1],[1],[1],[1],[1]]
C = [[1]]*A.shape[0]
def getRanges(row):
	global A
	return range(1,torch.sum(A[row]!=0)+1)
# B = torch.Tensor(B)
C = torch.Tensor(C)

def calcVal(mat):
	cnt = 0
	for x in mat:
		if(x==0.0 or x==1.0):
			continue

		# cnt+=(x+1-x)/2
		cnt+=max(0-x,1-x)
	return int(cnt)
def DiffRet(a,b):
	return torch.sum((b-a))
def printMe(vals,ret_=False):
	a,b,c,d = vals
	C = [[a],[b],[c],[d]]
	C = torch.Tensor(C)
	# print(C)
	# print(torch.mm(B,A))
	# print(torch.inverse(A))
	ret = (torch.mm(torch.inverse(A),C))
	if(ret_):
		print(vals)
		print(ret)
	# if(not is_decimal(ret)):
	# print(a,b,c,d)
	# print(ret)
	# print("Val",calcVal(ret))
	return calcVal(ret)
	# print(list(x for x in ret))
	# print(is_decimal(ret))
vals = [1]*4
print(vals)
mina = printMe(vals)
for i in range(4):
	vals[i]+=1
	if(printMe(vals,ret_=False)>=mina):
		vals[i]-=1
mina = printMe(vals)
for i in range(4):
	vals[i]+=1
	if(printMe(vals,ret_=False)>=mina):
		vals[i]-=1
print(vals)
printMe(vals,ret_=True)
# print(printMe([1,1,1,1],ret_=True))
# print(printMe([1,1,2,1],ret_=True))
# ret2 = printMe(1,1,2,1,ret_=True)
# ret3 = printMe(1,2,1,1)
# ret3 = printMe(1,3,1,1)
# print(DiffRet(ret2,ret3))