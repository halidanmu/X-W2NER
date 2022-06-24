# -*- coding:utf-8 -*-
"""
author: Chang Liu
date: 2022year04month18day
"""
import json
from sklearn.metrics import classification_report,precision_recall_fscore_support
results = open (r"output.json",'r', encoding='utf-8')
results_list = json.load(results)
results.close()

print(results_list[3])
print(results_list[14])
print(results_list[18])

y_pred=[]
y_pred2=[]
y_true=[]
y_true2=[]

for results_dict in results_list:
    predict_sent = []
    for text_type in results_dict["entity"]:
        if len(text_type["text"])==1:
            predict_sent.append("s")
        elif len(text_type["text"])==2:
            predict_sent.extend(["b","e"])
        elif len(text_type["text"])>=3:
            predict_sent.extend(["b"])
            predict_sent.extend((len(text_type["text"])-2)*["m"])
            predict_sent.extend("e")
        #if :
    y_pred.extend(predict_sent)
    y_pred2.append(predict_sent)

true=open(r'/root/autodl-nas/liuchang/baseline/THUUMS/data/test.trg','r',encoding='utf-8')
true1=true.readlines()
true.close()
list1=[]
for i in true1:
    data = i.split()
    list1.append(data)
for j in list1:
    y_true.extend(j)
    y_true2.append(j)
#print(precision_recall_fscore_support(y_true, y_pred, average='macro',labels=['b', 'm', 'e', 's']))

for i in range(len(y_pred2)):
    if len(y_pred2[i])!=len(y_true2[i]):
        print(i)
        print(y_pred2[i])
        print(y_true2[i])

print(classification_report(y_true = y_true,
                                y_pred = y_pred,
                                labels=['b', 'm', 'e', 's'],
                                digits=5))