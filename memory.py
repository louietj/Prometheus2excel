import requests
import xlwt
import xlrd
from xlutils.copy import copy
import numpy as np
import write_excel
import time

def output_memory(metric,start_time,end_time,step):
    parameter = {'query': metric, 'start': start_time, 'end': end_time, 'step': step}
    ret = requests.get("http://172.26.0.5:31601/api/v1/query_range", params=parameter)
    len_data = ret.text.count('values', 0, len(ret.text))
    GPSType=np.dtype({'names':['0','1','2','3','4','5'],'formats':['S64','S64','S64','float_','float_','float_']})
    Data=np.array([(None,None,None,None,None,None)]*len_data,dtype=GPSType)  #创建Data[2]

    length=len(ret.text)
    n=0
    j=0
    i=0
    j_temp=0
    value_temp=[]
    while i<length:

        if ret.text[i:i + 9] == "namespace":
        #Data[n]['instance'] =ret.text[i+11:i+26]
        #i=i+26
            j=i+12
            j_temp=j
            while(ret.text[j]!='"'):
                j=j+1
        #print(ret.text[j_temp:j])
            Data[n]['0']=ret.text[j_temp:j]
            i=j-1
        elif ret.text[i:i + 8] == "pod_name":
        #Data[n]['instance'] =ret.text[i+11:i+26]
        #i=i+26
            j=i+11
            j_temp=j
            while(ret.text[j]!='"'):
                j=j+1
        #print(ret.text[j_temp:j])
            Data[n]['2']=ret.text[j_temp:j]
            i=j-1
        elif ret.text[i:i + 8] == "instance":
        #Data[n]['instance'] =ret.text[i+11:i+26]
        #i=i+26
            j=i+11
            j_temp=j
            while(ret.text[j]!=':'):
                j=j+1
        #print(ret.text[j_temp:j])
            Data[n]['1']=ret.text[j_temp:j]
            i=j-1
        elif ret.text[i:i + 6] == "values":
            j=i+7
            while(1):
                if ret.text[j]=='}':
                    break
                elif ret.text[j]=='"':
                    j_temp=j+1
                    j=j_temp
                    while (ret.text[j] != '"'):
                        j = j + 1
                    value_temp.append(float(ret.text[j_temp:j]))
                j=j+1    #j=j+1
            Data[n]['3'] = max(value_temp)
            Data[n]['4'] = np.mean(value_temp)
            Data[n]['5'] = np.min(value_temp)
            value_temp.clear()
            i=j-1
            n=n+1
        else:
            i=i+1





    return Data


#p=1






