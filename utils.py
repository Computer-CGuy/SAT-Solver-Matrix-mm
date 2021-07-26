import torch
def listToInt(vals):
    return list(map(int,vals))
def sgn(i):
    return (-1 if i<0 else 1)
def read_cnf_from_file(file_name):
    f = open(file_name,"r")
    # line = (line.strip())
    clause_id = 0
    for line in f:
        line = (line.strip())
        if line[0]=="c": continue
        if line[0]=="p":
            variables, clauses = line.replace("p cnf ","").split(" ")
            variables, clauses = int(variables),int(clauses)
            # shape = max(variables,clauses)
            shape = max(variables,clauses)
            shape+=1
            A = torch.zeros((variables+1,clauses))
            continue
        vals = listToInt(line.split(" "))[:-1]
        negs = 0
        print(vals)
        for x in vals:
            sgn_ = 1
            if(x==0): raise TypeError
            if(x<0): negs+=1; sgn_=-1; x = abs(x)
            try:
                A[clause_id][x-1]= sgn_
            except IndexError:
                A[clause_id-1][-1] = negs
                A[-1][-1] = 1
                return A
        A[clause_id][-1] = negs
        clause_id+=1
    A[-1][-1] = 1
    return A
        

# ret = read_cnf_from_file("aim-50-1_6-yes1-4.cnf")
# ret = read_cnf_from_file("simple_v3_c2.cnf")
ret = read_cnf_from_file("simple.cnf")
# print(ret)

# ret = \
# torch.Tensor([[1., 1., 0., 0., 0., 0., 0., 0., 0.],
#         [0., 0., 1., 1., 0., 0., 0., 0., 0.],
#         [1., 1., 0., 0., 0., 0., 0., 0., 0.],
#         [1., 1., 0., 0., 0., 0., 0., 0., 0.],
#         [0., 0., 1., 0., 1., 0., 0., 1., 0.],
#         [0., 1., 1., 0., 0., 0., 0., 1., 0.],
#         [0., 0., 0., 1., 1., 0., 0., 1., 0.],
#         [0., 0., 0., 0., 1., 1., 1., 1., 0.],
#         [0., 0., 0., 0., 0., 0., 0., 0., 1.]])
# # ret[-2,-3:]=1
# ret[6,-1]=1
# print(ret)
# 1 2 3 0 
# 3 4 5 0
# 1 2 4 0
# 1 2 5 0
# 3 5 6 0
# 2 3 4 0
# 4 5 6 0
C = 7*[[3]]+[[1]]
C = [[2],[2],[1],[2],[2],[1],[1],[1]]
print(torch.mm(torch.pinverse(ret),torch.Tensor(C)))