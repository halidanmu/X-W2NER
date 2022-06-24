# -*- coding:utf-8 -*-
"""
author: Chang Liu
date: 2022year03month15day
"""
from datasets import load_dataset
import json
#dataset = load_dataset('/root/autodl-nas/liuchang/baseline/packages/wikiann.py','ug',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
#dataset = load_dataset('/root/autodl-nas/liuchang/baseline/packages/conll2003.py',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset = load_dataset("conll2003")
#print(dataset['test'][2])
#print(dataset['test'][2]['tokens'])
#print(type(dataset['test'][0]))

json_list=[]


tags=["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-MISC", "I-MISC"]


for id in dataset["test"]:
    ner_list = []
    json_dict = {}
    json_dict["sentence"] = id["tokens"]
    dataset_tags = id["ner_tags"]

    for num, tag_num in enumerate(dataset_tags):
        index_type = {}
        index_type["index"] = []
        if tag_num == 1:
            index_type["index"].append(num)
            if num != len(dataset_tags):
                for i in range(num + 1, len(dataset_tags)):
                    if dataset_tags[i] == 2:
                        index_type["index"].append(i)
                    else:
                        break
            #index_type["index"].extend(range(num,i))

            index_type["type"] = "PER"
            ner_list.append(index_type)
        elif tag_num == 3:
            index_type["index"].append(num)
            if num != len(dataset_tags):
                for i in range(num + 1, len(dataset_tags)):
                    if dataset_tags[i] == 4:
                        index_type["index"].append(i)
                    else:
                        break
            #index_type["index"].extend(range(num,i))
            index_type["type"] = "ORG"
            ner_list.append(index_type)
        elif tag_num == 5:
            index_type["index"].append(num)
            for i in range(num + 1, len(dataset_tags)):
                if dataset_tags[i] == 6:
                    index_type["index"].append(i)
                else:
                    break
            #index_type["index"].extend(range(num,i))

            index_type["type"] = "LOC"
            ner_list.append(index_type)
        elif tag_num == 7:
            index_type["index"].append(num)
            for i in range(num + 1, len(dataset_tags)):
                if dataset_tags[i] == 8:
                    index_type["index"].append(i)
                else:
                    break
                #index_type["index"].extend(range(num,i))
            index_type["type"] = "MISC"
            ner_list.append(index_type)
        else:
            continue
        #if ner_list != None:
        json_dict["ner"] = ner_list
    json_list.append(json_dict)
#print(json_list[0])
#print(json_list[1])
with open("/mnt/d/experiments/conll03-w2ner/conll03/test.json","r") as json_file:
    json_dict2 = json.load(json_file)
#print(json_dict[0])

#print(type(json_list))
#print(type(json_dict2))
print(len(json_list)==len(json_dict2))
'''
for a in range(len(json_list)):
    if json_list[a] != json_dict2[a]:
        print(a)

print(json_list[3451])
print(json_dict2[3451])
'''