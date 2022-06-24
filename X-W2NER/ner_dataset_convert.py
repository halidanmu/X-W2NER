# -*- coding:utf-8 -*-
"""
author: Chang Liu
date: 2022year03month15day
"""
from datasets import load_dataset, DatasetDict, concatenate_datasets
import json


dataset = load_dataset("wikiann","uz",cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
'''
dataset1 = load_dataset('wikiann','az',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset2 = load_dataset('wikiann','kk',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset3 = load_dataset('wikiann','ky',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset4 = load_dataset('wikiann','tr',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset5 = load_dataset('wikiann','ug',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset6 = load_dataset('wikiann','uz',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')
dataset7 = load_dataset('wikiann','en',cache_dir='/root/autodl-nas/liuchang/huggingface/transformers')

def concatenate_splits(corpora):
    multi_corpus = DatasetDict()
    for split in corpora[0].keys():
        multi_corpus[split] = concatenate_datasets(
                [corpus[split] for corpus in corpora]).shuffle(seed=42)
    return multi_corpus
dataset = concatenate_splits([dataset1, dataset2, dataset3, dataset4, dataset5, dataset6, dataset7])
'''



json_list=[]


tags=["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC"]


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
            
            index_type["type"] = "ORG"
            ner_list.append(index_type)
        elif tag_num == 5:
            index_type["index"].append(num)
            for i in range(num + 1, len(dataset_tags)):
                if dataset_tags[i] == 6:
                    index_type["index"].append(i)
                else:
                    break
            

            index_type["type"] = "LOC"
            ner_list.append(index_type)
        else:
            continue
        
        json_dict["ner"] = ner_list
    json_list.append(json_dict)


with open("/root/autodl-nas/liuchang/W2NER/data/uz_tr_ner/test.json","w") as json_file:
    json.dump(json_list, json_file)
