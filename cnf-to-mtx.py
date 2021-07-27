from pycryptosat import Solver
import time
s = Solver()

solver = Solver()

with open("../input/cnfstimestamped/test-nonceTVA.cnf", "r") as x:
    for i,line in enumerate(x):
        line = line.strip()
        # if(line[0]=="p" or line[0]=="c"):
        if "p" in line or "c" in line:
            continue

        out = [int(x) for x in line.split()[:-1]]
        # solver.add_clause(out)
#         print(out)
        if(i==655665-1): # line no. 655243
            st=out
        elif(i==655666-1):
            end = out
        elif(i==655667-1):
            timestamp = out
        else:
            solver.add_clause(out)
def deform(clause,val):
    val = list((bin(val)[2:]).zfill(32))
    
    val = val[::-1]
    
    for i in range(len(clause)-1):
        clause[i] = abs(clause[i])
        if(val[i]=="0"):
            clause[i]*=-1
    return clause

def check(solver,start_nonce,end_nonce,time_):
#     print(id(solver))
    global st,end,timestamp
    st = deform(st,start_nonce)
    end = deform(end,end_nonce)
    timestamp = deform(timestamp,time_)
#     end_range = 497822589
    # end_range = 11
    start = time.time()
    isSAT, sols = solver.solve(st+end+timestamp)
    # res, isSAT = solver.solve()
    done = time.time()
    elapsed = done - start
    print(elapsed)
#     print(isSAT)
    return isSAT
print("checking")
print(check(solver,497822587,497822589,4294901789))