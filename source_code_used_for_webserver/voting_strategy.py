'''
get five kinds of voting strategy
'''
import numpy as np
import pandas as pd
PCP_path = 'PCP_predict.csv'
PSNP_path = 'PSNP_predict.csv'
GAC_RFH_path = 'RFHC_GAC_predict.csv'

PSNP = pd.read_csv(PSNP_path, header=None)
PSNP = PSNP.values
PSNP2 = PSNP
positive_ = [PSNP[index, 1] for index, e in enumerate(PSNP[:, 0]) if e == 1]
negative_ = [PSNP[index, 1] for index, e in enumerate(PSNP[:, 0]) if e == 0]
positive_.extend(negative_)
PSNP = np.array(positive_).astype(int)

positive_prob = [PSNP2[j, 2] for j, e in enumerate(PSNP2[:, 0]) if e == 1]
negative_prob = [PSNP2[j, 2] for j, e in enumerate(PSNP2[:, 0]) if e == 0]
positive_prob.extend(negative_prob)
PSNP_prob = np.array(positive_prob)

PCP = pd.read_csv(PCP_path, header=None)
PCP = PCP.values
PCP2 = PCP
positive_ = [PCP[index, 1] for index, e in enumerate(PCP[:, 0]) if e == 1]
negative_ = [PCP[index, 1] for index, e in enumerate(PCP[:, 0]) if e == 0]
positive_.extend(negative_)
PCP = np.array(positive_).astype(int)

positive_prob = [PCP2[j, 2] for j, e in enumerate(PCP2[:, 0]) if e == 1]
negative_prob = [PCP2[j, 2] for j, e in enumerate(PCP2[:, 0]) if e == 0]
positive_prob.extend(negative_prob)
PCP_prob = np.array(positive_prob)

GAC_RFH_ = pd.read_csv(GAC_RFH_path, header=None)
GAC_RFH_ = GAC_RFH_.values
GAC_RFH2 = GAC_RFH_
positive_ = [GAC_RFH_[index, 1] for index, e in enumerate(GAC_RFH_[:, 0]) if e == 1]
negative_ = [GAC_RFH_[index, 1] for index, e in enumerate(GAC_RFH_[:, 0]) if e == 0]
positive_.extend(negative_)
GAC_RFH_ = np.array(positive_).astype(int)

positive_prob = [GAC_RFH2[index, 2] for index, e in enumerate(GAC_RFH2[:, 0]) if e == 1]
negative_prob = [GAC_RFH2[index, 2] for index, e in enumerate(GAC_RFH2[:, 0]) if e == 0]
positive_prob.extend(negative_prob)
GAC_RFH_prob = np.array(positive_prob)



final_prob = (PCP_prob + PSNP_prob + GAC_RFH_prob) / 3


final_result = GAC_RFH_ + PSNP + PCP
y_pred = [1 if e >= 2 else 0 for e in final_result]
y_true = [1 if index < len(final_result) / 2 else 0 for index, e in enumerate(final_result)]
output_result = []
output_result.append(np.array(y_true).astype(int))
output_result.append(np.array(final_result / 2).astype(int))
output_result.append(final_prob)
output_result = np.array(output_result).T
pd.DataFrame(output_result).to_csv('voting_strategy.csv', header=None,index=False)

