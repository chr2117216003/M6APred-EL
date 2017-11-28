'''
fetch PSNP feature
'''


import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import *
seq=[]

m6a_2614_sequence="in.txt"


RNA_code='ACGU'
k=1
interval=1
divided_num=10.0
division_num=10
fh=open(m6a_2614_sequence)
for line in fh:
    if line.startswith('>'):
        pass
    else:
        seq.append(line.replace('\r\n',''))
fh.close()
def make_kmer_list(k, alphabet):
    try:
        return ["".join(e) for e in itertools.product(alphabet, repeat=k)]
    except TypeError:
        print("TypeError: k must be an inter and larger than 0, alphabet must be a string.")
        raise TypeError
    except ValueError:
        print("TypeError: k must be an inter and larger than 0")
        raise ValueError
positive_seq=seq[:int(len(seq)/2)]
negative_seq=seq[int(len(seq)/2):]
kf = KFold(n_splits=division_num,shuffle=False)
code_values=make_kmer_list(1,RNA_code)
code_len=len(code_values)
PSNP_data=[[0 for ii in xrange(len(seq[0])-interval)] for jj in xrange(len(seq))]
positive_seq_value=pd.read_csv('positive_seq_value_',index_col=False,header=None)
positive_seq_value=positive_seq_value.values
negative_seq_value=pd.read_csv('negative_seq_value_',index_col=False,header=None)
negative_seq_value=negative_seq_value.values
for i,line_value in enumerate(seq):
    for j,code_value in enumerate(line_value):
        if j<= len(line_value)-interval-1:
            for p,c_value in enumerate(code_values):
                if c_value==line_value[j:j+1]:
                    PSNP_data[i][j]=positive_seq_value[p,j]-negative_seq_value[p,j]
pd.DataFrame(PSNP_data).to_csv('PSNP.csv',header=None,index=False)