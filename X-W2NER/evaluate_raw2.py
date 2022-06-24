# -*- coding:utf-8 -*-
"""
author: Chang Liu
date: 2022year05month10day
"""
import json
from sklearn.metrics import classification_report,precision_recall_fscore_support
results = open (r"output.json",'r', encoding='utf-8')
results_list = json.load(results)
results.close()

for results_dict in results_list:
    morph_list=[]
    for text_type in results_dict["entity"]:
        morph_list.extend(text_type["text"])
    if morph_list != results_dict["sentence"]:
        print("false")

    if len(results_dict["sentence"]) != len(results_dict["entity"]):
        print("False")

#print(results_list[3])
#print(results_list[14])
#print(results_list[18])

y_pred=[]
y_pred2=[]
y_true=[]
y_true2=[]

label_list = []
for results_dict in results_list:
    label_list0 = []
    for text_type in results_dict["entity"]:
        label_list0.append(text_type["type"])
    label_list.append(label_list0)


for j in range(len(label_list)):
    for k in range(len(label_list[j])):
        if label_list[j][k] == "m" and (k == len(label_list[j])-1 or label_list[j][k + 1] == "s" or label_list[j][k + 1] == "b" ):
            label_list[j][k] = "e"
        elif label_list[j][k] == "b" and (k == len(label_list[j])-1 or label_list[j][k + 1] == "b"):
            label_list[j][k] = "s"
for i in label_list:
    y_pred.extend(i)
'''
for results_dict in results_list:
    label_list = []
    for text_type in results_dict["entity"]:
        label_list.append(text_type["type"])

        for i in range(len(label_list)):
            if label_list[i] == "m" and (i==len(label_list)-1 or label_list[i+1] == "s" or label_list[i+1] == "b"):
                label_list[i] = "e"
            elif label_list[i] == "b" and (i==len(label_list)-1 or label_list[i+1] == "b"):
                label_list[i] = "s"
        #if :
    y_pred.extend(label_list)
    y_pred2.append(label_list)
'''

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