'''
fetch RFH_without_GAC
'''

from __future__ import division
def convert():
    """RFH feature"""
    dataPath= "in.txt"
    lines=open(dataPath).readlines()
    outputPath="RFHC_GAC.csv"
    classifier_type='U'#sys.argv[3]
    finally_text = open(outputPath, 'w')
    finnaly_lines=""
    for line in lines:
        if line.strip()=="":continue
        if line.strip()[0] in ['A','G','C',classifier_type]:
            position_mark=0
            count_AGCT=[0,0,0,0]
            temp = ""
            one_line=list(line.strip())
            for i,x in enumerate(one_line):
                if i!=24 and i!=25 and i!=26:
                    position_mark+=1
                    if x=="A" or x=="G":temp+="1,"
                    else:temp+="0,"
                    if x=="A" or x==classifier_type:temp+="1,"
                    else:temp+="0,"
                    if x == "A" or x == "C":temp+="1,"
                    else:temp+="0,"
                    if x == "A":
                        count_AGCT[0] += 1
                        temp +=str(round(count_AGCT[0] / position_mark*1.0,2))
                        temp+=','
                    elif x == "G":
                        count_AGCT[1] += 1
                        temp +=str(round(count_AGCT[1] / position_mark*1.0,2))
                        temp += ','
                    elif x == "C":
                        count_AGCT[2] += 1
                        temp +=str(round(count_AGCT[2] / position_mark*1.0,2))
                        temp += ','
                    elif x == classifier_type:
                        count_AGCT[3] += 1
                        temp +=str(round(count_AGCT[3] / position_mark*1.0,2))
                        temp += ','

            finnaly_lines+=((temp[:len(temp)-1])+'\n')
            #finally_text.write(temp+'\n')
    finally_text.writelines(finnaly_lines)
    finally_text.close()
convert()