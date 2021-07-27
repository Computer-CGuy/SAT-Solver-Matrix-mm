import torch
from utils import read_cnf_from_file


A = read_cnf_from_file("simple_v3_c2.cnf")
print(A)