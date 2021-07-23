import torch

# a b d 0
# -b c d 0
# -b -c d 0
A = [[1,1,0,1,0],
	 [0,-1,1,1,1],
	 [0,-1,-1,1,2],
	 [1,0,0,0,0],
	 [0,0,0,0,1]]
# B = [[1],[1],[1]]
def is_decimal(tensor):
	if(torch.all(tensor.long()==tensor)):
		return False
	else:
		return True

C = [[1],[1],[1],[1],[1]]

A = torch.Tensor(A)
# B = torch.Tensor(B)
C = torch.Tensor(C)

vals = range(1,3)

for a in vals:
	for b in vals:
		for c in vals:
			for d in vals:
				for e in vals:
					C = [[a],[b],[c],[d],[e]]
					C = torch.Tensor(C)
					# print(torch.mm(B,A))
					# print(torch.inverse(A))
					ret = (torch.mm(torch.inverse(A),C))
					if(not is_decimal(ret)):
						print(a,b,c,d,e)
						print(ret)
						print(is_decimal(ret))
