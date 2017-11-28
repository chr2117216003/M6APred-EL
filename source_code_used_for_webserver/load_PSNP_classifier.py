# !/use/bin/env python
# encoding:utf-8
import pandas as pd
import numpy as np
import joblib

'''
PSDNP_1gap load joblib
'''
divided_num=1.0
#define variable to save data which will be saved later --- begining
y_pred_prob_all=[]
y_pred_all=[]
Y_all=[]
#define variable to save data which will be saved later --- end



clf=joblib.load('PSNP.model')
PCP_data=pd.read_csv('PSNP.csv',header=None,index_col=False)
PCP_data=PCP_data.values
y_true=[1 if index<PCP_data.shape[0]//2 else 0 for index,e in enumerate(PCP_data)]
y_pred_prob=clf.predict_proba(PCP_data)
y_pred=clf.predict(PCP_data)
y_pred_prob_all.extend(y_pred_prob)
y_pred_all.extend(y_pred)
Y_all.extend(y_true)
all_y=[np.array(Y_all).astype(int),np.array(y_pred_all).astype(int),np.array(y_pred_prob_all).astype(list)[:,1]]
pd.DataFrame(np.matrix(all_y).T).to_csv('PSNP_predict.csv',header=None,index=False)


