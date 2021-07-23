import torch
# 16 17 30 0
# -17 22 30 0
# -17 -22 30 0

A = [[1,1,0],
	 [0,1,0],
	 [0,0,1]]
# B = [[1],[1],[1]]
C = [[2],[2],[2]]

A = torch.Tensor(A)
# B = torch.Tensor(B)
C = torch.Tensor(C)

# print(torch.mm(A,B))
print(torch.mm(torch.inverse(A),C))
