import torch
# torch.set_printoptions(precision=3)
def listToInt(vals):
    return list(map(int,vals))
def sgn(i):
    return (-1 if i<0 else 1)
def safePrint(matrix):
    matrix[matrix<0.001]=0
    print(matrix)
num_clauses = 0
def read_cnf_from_file(file_name):
    global num_clauses
    f = open(file_name,"r")
    # line = (line.strip())
    clause_id = 0
    for line in f:
        line = (line.strip())
        if line[0]=="c": continue
        if line[0]=="p":
            variables, clauses = line.replace("p cnf ","").split(" ")
            variables, clauses = int(variables),int(clauses)
            num_clauses = clauses
            # shape = max(variables,clauses)
            
            # A = torch.zeros((variables+2,clauses))
            A = torch.zeros((clauses+1,variables+1))
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
                print("Index Error")
                A[clause_id-1][-1] = negs
                A[-1][-1] = 1
                return A
        A[clause_id][-1] = negs
        clause_id+=1
    A[-1][-1] = 1
    return A
        

# ret = read_cnf_from_file("aim-50-1_6-yes1-4.cnf")
ret = read_cnf_from_file("simple_v3_c2.cnf")
# ret = read_cnf_from_file("simple.cnf")
# ret = read_cnf_from_file("simple.cnf")
# print(ret)

C = 7*[[3]]+[[1]]

C = [[2],[2],[1],[2],[2],[1],[1],[1]]
C = (num_clauses)*[[1]]+[[1]]
print(ret)
ans = torch.mm(torch.pinverse(ret),torch.Tensor(C))
safePrint(ans)
# print()