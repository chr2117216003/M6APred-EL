fetch_PCP_feature.py,fetch_PSNP_feature.py,fetch_RFHC_GAC_feature.py are used for fetch 
features from original sequences, where PSNP means PS(1-mer)NP in the paper[1] and default 
input filename is "in.txt" which is in the same directory of the code. It is also the place 
where save the input information of user.And the outputs are PCP.csv,PSNP.csv,RFHC_GAC.csv,
respectively.

load_PCP_classifier.py,load_PSNP_classifier.py and load_RFHC_GAC_classifier.py are used for generating 
predict labels of each sample, which will be save in PCP_predict.csv,PSNP_predict.csv and RFHC_GAC_predict.csv,
 respectively.
 
after obtaining all these Y true label, Y predict label and Y predict probability, it can be used 
for voting and generating finally predict label, which is loaded in voting_strategy.csv after running
voting_strategy.py program.



